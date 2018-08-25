# Constants for working with Union student data

# Grades rank order
grade_to_point = {'A':4.0, 'A-':3.7, 'B+':3.3, 'B':3.0, 'B-':2.7, 'C+':2.3,
                  'C':2.0, 'C-':1.7, 'D': 1.0, 'F':0.0, 'NC':None, 'P': None}
grade_rank = ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D', 'F']
point_rank = [grade_to_point[grade] for grade in grade_rank]

# Terms - quarters
term_to_month = {'FA':9, 'WI':1, 'SP':4, 'SU':7}
term_order_nosu = ['FA', 'WI', 'SP']

# Course groups
#   Somewhat arbitrary groups based on major requirements:
#     https://muse.union.edu/mathematics/program/major-minor/
#   note: intro courses split into three paths and may also be satisified 
#         with AP credit, first path (MTH-100 -101, -102) excluded as it is
#         uncommon for majors
#   note: 497 or 498 and 499 are senior theses. P (pass) is give to 498
#         instead of a letter grade
courses_intro = ['MTH-110', 'MTH-112','MTH-113']
courses_core =  ['MTH-115', 'MTH-115H', 'MTH-117', 'MTH-199', 'MTH-332', 
                 'MTH-336', 'MTH-340']
courses_thesis = ['MTH-497', 'MTH-499']
courses_select = courses_intro + courses_core + courses_thesis
