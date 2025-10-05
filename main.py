import pandas as pd
from utils.model import TutorAssignmentModel


if __name__ == "__main__":
    DATA_PATH = "./data/small_data.xlsx"

    # Load specific sheets
    new_student_info = pd.read_excel(DATA_PATH, sheet_name="New Students")
    tutors = pd.read_excel(DATA_PATH, sheet_name="Tutor Information")
    existing_student_info = pd.read_excel(DATA_PATH, sheet_name="Existing Students")
    existing_student_info_filtered = existing_student_info[existing_student_info['active'] == True]

    optimizer = TutorAssignmentModel(
        new_students=new_student_info,tutor_info=tutors,
        existing_students=existing_student_info_filtered
        )
    
    optimizer.main_process()