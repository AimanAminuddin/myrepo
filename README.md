# myrep
HTX xData Technical Question-Data Scientist

# Tutor Assignment Optimization

## Background Information

A tutoring organisation with multiple tuition centres admits a fresh batch of students every month. New students are each assigned to a tutor and attend classes at one of the centres, as chosen by the student. Tutors on the other hand are free to teach at any centre and have indicated their top 2 preference. Before the start of a new month, the organization assigns a tutor to each new incoming student, meeting specific requirements.

## Student-Tutor Assignment Constraint(s)

1. **Single Tutor Assignment**  
   Each student can only be assigned **one tutor**.

2. **Tutoring Needs**  
   - Some students require **extensive tutoring** due to poor academic performance.  
   - Not all tutors are equipped for extensive tutoring. Tutor skills are classified as **normal** or **extensive**.  
   - Students requiring extensive tutoring can only be assigned to tutors labelled as extensive.  
   - Students requiring normal tutoring can be assigned to either type of tutor.

3. **Tutor Capacity**  
   - Each tutor has a **maximum overall capacity**.  
   - The total number of students assigned (new + existing) **cannot exceed the tutor's maximum overall capacity**.

## Objectives

To formulate and solve this Integer Programming problem for 2 scenarios/use cases:

1. **Minimize total number of tutors assigned while maximizing tutor's preference on tuition centre 

2. **Balance tutor's workload while maximizing tutor's preference on tuition centre**

## Approach

The problem is modeled using **Python** and the **docplex** library with IBM CPLEX Community Edition.

## Key Components


1. **Decision Variables**
   - `assign_vars[student_id, tutor_id]`: Binary variable indicating if a student is assigned to a tutor.  
   - `tutor_used[tutor_id]`: Binary variable indicating if a tutor is assigned any student.

2. **Constraints**
   - Each student is assigned **exactly one tutor**.  
   - Tutors’ **capacity limits** are not exceeded.  
   - **Skill compatibility:** Students needing extensive tutoring are assigned only to suitable tutors.  
   - `tutor_used` ensures that a tutor is considered “used” if any student is assigned.

3. **Objective Functions**
   - **Scenario 1:** Maximize tutor preference while minimizing tutors used.  
   - **Scenario 2:** Maximize tutor preference while **balancing workload** (minimizing free capacity)


---

## Outputs & Post-Processing
Before Optimization, non-active students are filtered out to prevent overcounting existing students assigned to tutors. After optimization, the following reports are generated:

1. **Student-Tutor-Assignments**
   - Generate a csv file containing the assignment of students to different tutors
   - Columns: `StudentID`,`TutorID`
   - Assignments are saved for each scenario mentioned in the task:
	- `scenario_1_assignment_results.csv`
	- `scenario_2_assignment_results.csv`

2. **Tutor Summary Report**
   - Columns: `TutorID`, `NewAssigned`, `Existing`, `TotalAssigned`, `MaxCapacity`, `FreeCapacity`   

3. **Preference Report**
   - Lists each student’s tuition centre against the assigned tutor’s top 2 preferred centres.  
   - Includes a boolean indicating if the assignment matches one of the tutor’s preferred centres.

4. **CSV Export**
   - Reports are saved for each scenario:  
     - `scenario_1_{name of the report}.csv`  
     - `scenario_2_{name of the report}.csv`

---

## Setup & Run Instructions

1. **Install IBM CPLEX Community Edition**
   - Download from: https://www.ibm.com/products/ilog-cplex-optimization-studio  
   - Follow installation instructions for your OS.
   - Make sure the CPLEX Python API is installed (usually via `pip install cplex` or through the CPLEX Python setup script).

2. **Set Environment Path (if needed)**
   - Ensure the `cplex` shared library is in your system path.
   - Example (Linux/macOS):
     ```bash
     export PYTHONPATH=/opt/ibm/ILOG/CPLEX_Studio221/python/3.11/x64_linux:$PYTHONPATH
     export PATH=/opt/ibm/ILOG/CPLEX_Studio221/cplex/bin/x64_linux:$PATH
     ```
   - Example (Windows PowerShell):
     ```powershell
     setx PYTHONPATH "C:\Program Files\IBM\ILOG\CPLEX_Studio221\python\3.11\x64_win64"
     setx PATH "C:\Program Files\IBM\ILOG\CPLEX_Studio221\cplex\bin\x64_win64;%PATH%"
     ```

3. **Create & activate Python virtual environment**

Run the following commmands to set up the virtual environment
```
# Create a python virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate # Linux/macOS
venv\Scripts\activate # Windows

# Install required packages
pip install -r requirements.txt

# Run the main script
python main.py

# Read the notebook: TutorAssignment.ipynb for model results
```
---
