from models import db, Module
import pandas as pd
from services.populate_timeslotstable import run as ts_run

def run():
    modules_df = pd.read_csv("utils/csv/dut_modules.csv")

    for index, row in modules_df.iterrows():
        module_name = row['module_name']
        module_code = row['module_code']

        new_module = Module(module_name=module_name, module_code=module_code)
        db.session.add(new_module)

    db.session.commit()
    db.session.flush()
    all_modules = db.session.query(Module).all()
    #create timeslots at random for all modules
    ts_run(all_modules)