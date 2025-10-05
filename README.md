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
