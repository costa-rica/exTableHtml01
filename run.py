from flask import Flask, request, render_template
from ws_models01 import sess, Apple_health_export
from ws_config01 import ConfigDev
import pandas as pd
import os

app = Flask(__name__)
app.debug = True

config = ConfigDev()

@app.route("/", methods=["GET","POST"])
def index():
    return render_template("index.html")


@app.route("/table_cdn", methods=["GET","POST"])
def table_cdn():
    USER_ID = 12
    file_name = f'user{USER_ID}_df_browse_apple.pkl'
    # file_path = os.path.join(config.DF_FILES_DIR, file_name)
    file_path = os.path.join("/Users/nick/Documents/_databases/ws08/df_files", file_name)

    print(os.path.abspath(file_path))

    df = pd.read_pickle(file_path)
    df['index'] = range(1,len(df)+1)

    df_list_of_rw_dicts = df.to_dict('records')

    col_names = ['index', 'Name','Type', 'Count', 'df_exists']
    print(col_names)

    


    return render_template("table_cdn.html", df = df_list_of_rw_dicts, col_names=col_names)


@app.route("/table", methods=["GET","POST"])
def table():
    USER_ID = 12
    file_name = f'user{USER_ID}_df_browse_apple.pkl'
    # file_path = os.path.join(config.DF_FILES_DIR, file_name)
    file_path = os.path.join("/Users/nick/Documents/_databases/ws08/df_files", file_name)

    print(os.path.abspath(file_path))

    df = pd.read_pickle(file_path)
    df['index'] = range(1,len(df)+1)

    df_list_of_rw_dicts = df.to_dict('records')

    col_names = ['index', 'Name','Type', 'Count', 'df_exists']
    print(col_names)

    


    return render_template("table.html", df = df_list_of_rw_dicts, col_names=col_names)





if __name__ == "__main__":
    app.run()

