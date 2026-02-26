
# У цьому файлі зберігаються всі дані в пам'яті

users = []       # {"username":..., "password":..., "role":"teacher/student"}
subjects = []    # {"id":1, "name":...}
classes = []     # {"id":1, "name":...}
teachers = []    # {"username":..., "subject_id":...}
students = []    # {"username":..., "class_id":...}
schedules = []   # {"subject_id":..., "teacher_username":..., "class_id":..., "day":..., "time":...}
grades = []      # {"student_username":..., "subject_id":..., "grade":...}