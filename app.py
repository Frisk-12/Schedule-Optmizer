#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 16:38:30 2024

@author: andreadesogus
"""

from flask import Flask, render_template, request, jsonify
from ortools.sat.python import cp_model

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    data = request.json
    employees = data['employees']
    absences = data['absences']
    preferences = data['preferences']

    # Modello OR-Tools
    model = cp_model.CpModel()
    num_days = 5
    num_shifts = 2
    hours_per_shift = 4
    max_hours_per_week = 40
    work = {}

    for e in employees:
        for d in range(num_days):
            for s in range(num_shifts):
                work[e, d, s] = model.NewBoolVar(f'work_{e}_{d}_{s}')

    for e in employees:
        for (d, s) in absences[e]:
            model.Add(work[e, d, s] == 0)

    for e in employees:
        for d in range(num_days):
            model.Add(sum(work[e, d, s] * hours_per_shift for s in range(num_shifts)) <= 8)

    for e in employees:
        model.Add(sum(work[e, d, s] * hours_per_shift for d in range(num_days) for s in range(num_shifts)) <= max_hours_per_week)

    for d in range(num_days):
        for s in range(num_shifts):
            model.Add(sum(work[e, d, s] for e in employees) >= 2)

    preference_score = sum(work[e, d, s] for e in employees for (d, s) in preferences[e])
    model.Maximize(preference_score)

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.OPTIMAL:
        result = {}
        for d in range(num_days):
            result[d] = {}
            for s in range(num_shifts):
                shift_name = "Morning" if s == 0 else "Evening"
                result[d][shift_name] = [e for e in employees if solver.BooleanValue(work[e, d, s])]
        return jsonify(result)
    else:
        return jsonify({"error": "No optimal solution found."})

if __name__ == '__main__':
    app.run(debug=True)
