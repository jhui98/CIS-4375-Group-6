# @wakindo
#======================================

# Flask imports
import flask
from flask import jsonify
from flask import request, make_response

# MySQL connector import
import mysql.connector
from mysql.connector import Error
import creds # My AWS DB credentials

# All other functions imports
from myFunctions import create_connection
from myFunctions import execute_query
from myFunctions import execute_read_query
# import hashlib # not needed yet
import datetime
import time
# Creating connection to mysql database
myCreds = creds.Creds()
conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)


# Setting up an application name
app = flask.Flask(__name__) # sets up the application
app.config["DEBUG"] = True # allow to show errors in browser

#=================================================
# Default url without any routing as GET request #
#=================================================
# (endpoint to home page: http://127.0.0.1:5000)
@app.route('/', methods=['GET'])
def home():
    return "<h1> Welcome to OVVI Shipping Management System v1.0! </h1>"


######################################################
# 1-  CRUD operations for the HARWARE_TYPE table     #
######################################################

#=========================================================#
# 1.1. - Implement GET method for all hardware_types here #
#=========================================================#
# Endpoint to GET all hardware_types http://127.0.0.1:5000/api/hardware_type/all
@app.route('/api/hardware_type/all', methods=['GET'])
def api_hardware_type_all():
    # select all hardware_types from DB
    # Add HTYPE_ID and use for Update/Delete but never show it on the frontend to user
    select_hardware_types = """
        SELECT htype_id, htype_name
        FROM hardware_type
        ORDER BY htype_name ASC; """ 

    hardware_types = execute_read_query(conn, select_hardware_types)
    results = [] # List of resulting hardware_type(s) to return
    for hardware_type in hardware_types:
        results.append(hardware_type)
    return jsonify(results)

#========================================================#
# 1.2 - Implement POST method for hardware_type here     #
#========================================================#
# Endpoint to ADD an hardware_type http://127.0.0.1:5000/api/hardware_type
@app.route('/api/hardware_type', methods=['POST'])
def add_hardware_type():
    request_data = request.get_json()
    new_htype_name = request_data['htype_name']
    
    add_hardware_type_query = """
    INSERT INTO hardware_type(htype_name) 
    VALUES('%s')""" % (new_htype_name)
    # print("Insert query is: ", add_hardware_type_query) // just checking query syntax
    execute_query(conn, add_hardware_type_query) 
    
    return 'Add request was successful'


#====================================================#
# 1.3 - Implement PUT method for hardware_type here     #
#====================================================#
# Endpoint to UPDATE an hardware_type http://127.0.0.1:5000/api/hardware_type (takes a JSON object and update hardware_type table)
@app.route('/api/hardware_type', methods=['PUT'])
def update_hardware_type():
    request_data = request.get_json()
    # hardware_type data to update 
    idToUpdate = request_data['htype_id']
    new_htype_name = request_data['htype_name']
    update_hardware_type_query = """
    UPDATE hardware_type
    SET htype_name = '%s'  
    WHERE htype_id = %s """ % (new_htype_name, idToUpdate)
    # print("Update query is: ", update_hardware_type_query) // just checking query
    execute_query(conn, update_hardware_type_query)

    return "Update request successful"

#====================================================#
# 1.4 - Implement DELETE method for hardware_type here   #
#====================================================#
# Endpoint to delete an hardware_type http://127.0.0.1:5000/api/hardware_type?id=x (takes an hardware_type ID and set isDelete to 'Y')
@app.route('/api/hardware_type', methods=['DELETE'])
def delete_hardware_type():
    if 'id' in request.args: # only if an ID is provided as an argument, proceed
        idToDelete = int(request.args['id']) # hardware_type ID to delete 
        delete_hardware_type_query = """
        DELETE FROM hardware_type 
        WHERE htype_id = %s """ % (idToDelete)
        # print("Update query is: ", delete_hardware_type_query)
        execute_query(conn, delete_hardware_type_query)
        return "Delete request was successful"
    else:
        return "No hardware_type ID provided"




# NB: ALWAYS remember to add this line or app won't run
app.run()




#========================================
# Test of all functionalities:          =
#========================================
#   Home page => OK
#   api/hardware_type (GET all) =>  OK
#   api/hardware_type (POST = INSERT INTO) => OK
#   api/hardware_type (PUT = UPDATE) => OK
#   api/hardware_type?id=x (Do a physical DELETE for now) => OK
