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


#===============================================================#
# 1.5. - Implement GET method for a specific hardware_type here #
#===============================================================#
# Endpoint to GET all hardware_types http://127.0.0.1:5000/api/hardware_type?id=x (takes an hardware_type ID and retrieve it from DB)
@app.route('/api/hardware_type', methods=['GET'])
def api_hardware_type_id():
    if 'id' in request.args: # only if an ID is provided as an argument, proceed
        idToRetrieve = int(request.args['id']) # hardware_type ID to Retrieve
        results = [] # List of resulting hardware_type(s) to return
        # Make SELECT only keep ID(s) matching the ID provided
        retrieve_hardware_type_query = """
        SELECT htype_id, htype_name 
        FROM hardware_type
        WHERE htype_id = %s ;""" % (idToRetrieve)
        # print("Select query is: ", retrieve_hardware_type_query) //just checking
        hardware_types  = execute_read_query(conn, retrieve_hardware_type_query)
        for hardware_type in hardware_types:
            if hardware_type['htype_id'] == idToRetrieve:
                results.append(hardware_type)
                #print(results) //checking results in console
        return jsonify(results)
    else:
        return "No hardware_type ID provided"
    


#####################################################
# 2-  CRUD operations for the HARDWARE table        #
#####################################################

#=========================================================#
# 2.1. - Implement GET method for all hardwares here      #
#=========================================================#
# Endpoint to GET all hardwares http://127.0.0.1:5000/api/hardware/all
@app.route('/api/hardware/all', methods=['GET'])
def api_hardware_all():
    # select all hardware_types from DB
    # Add HARDWARE_ID and use for Update/Delete but never show it on the frontend to user
    select_hardwares = """
        SELECT hardware_id, hardware_name,model_number, htype_id
        FROM hardware
        ORDER BY hardware_name ASC; """ 

    hardwares = execute_read_query(conn, select_hardwares)
    results = [] # List of resulting hardware(s) to return
    for hardware in hardwares:
        results.append(hardware)
    return jsonify(results)

#========================================================#
# 2.2 - Implement POST method for HARDWARE here          #
#========================================================#
# Endpoint to ADD an hardware_type http://127.0.0.1:5000/api/hardware
@app.route('/api/hardware', methods=['POST'])
def add_hardware():
    request_data = request.get_json()
    new_hardware_name = request_data['hardware_name']
    new_model_number = request_data['model_number']
    new_htype_id = request_data['htype_id']

    add_hardware_query = """
    INSERT INTO hardware(hardware_name, model_number, htype_id) 
    VALUES('%s', '%s', '%s')""" % (new_hardware_name, new_model_number,new_htype_id)
    # print("Insert query is: ", add_hardware_query) // just checking query syntax
    execute_query(conn, add_hardware_query) 
    
    return 'Add request was successful'


#====================================================#
# 2.3 - Implement PUT method for HARDWARE here       #
#====================================================#
# Endpoint to UPDATE an hardware_type http://127.0.0.1:5000/api/hardware (takes a JSON object and update hardware table)
@app.route('/api/hardware', methods=['PUT'])
def update_hardware():
    request_data = request.get_json()
    # hardware data to update 
    idToUpdate = request_data['hardware_id']
    new_hardware_name = request_data['hardware_name']
    new_model_number = request_data['model_number']
    new_htype_id = request_data['htype_id']

    update_hardware_query = """
    UPDATE hardware
    SET hardware_name = '%s',
        model_number = '%s',
        htype_id = '%s'
    WHERE hardware_id = %s """ % (new_hardware_name, new_model_number, new_htype_id, idToUpdate)
    # print("Update query is: ", update_hardware_query) // just checking query
    execute_query(conn, update_hardware_query)

    return "Update request successful"

#====================================================#
# 2.4 - Implement DELETE method for HARDWARE here    #
#====================================================#
# Endpoint to delete an hardware_type http://127.0.0.1:5000/api/hardware?id=x (takes an hardware ID and set isDelete to 'Y')
@app.route('/api/hardware', methods=['DELETE'])
def delete_hardware():
    if 'id' in request.args: # only if an ID is provided as an argument, proceed
        idToDelete = int(request.args['id']) # hardware_type ID to delete 
        delete_hardware_query = """
        DELETE FROM hardware 
        WHERE hardware_id = %s """ % (idToDelete)
        # print("Delete query is: ", delete_hardware_query)
        execute_query(conn, delete_hardware_query)
        return "Delete request was successful"
    else:
        return "No hardware ID provided"

#==========================================================#
# 2.5. - Implement GET method for a specific hardware here #
#==========================================================#
# Endpoint to GET all hardware_types http://127.0.0.1:5000/api/hardware?id=x (takes an hardware ID and retrieve it from DB)
@app.route('/api/hardware', methods=['GET'])
def api_hardware_id():
    if 'id' in request.args: # only if an ID is provided as an argument, proceed
        idToRetrieve = int(request.args['id']) # hardware_type ID to Retrieve
        results = [] # List of resulting hardware_type(s) to return
        # Make SELECT only keep ID(s) matching the ID provided
        retrieve_hardware_query = """
        SELECT hardware_id, hardware_name, model_number, htype_id 
        FROM hardware
        WHERE hardware_id = %s ;""" % (idToRetrieve)
        # print("Select query is: ", retrieve_hardware_query) //just checking
        hardwares  = execute_read_query(conn, retrieve_hardware_query)
        for hardware in hardwares:
            if hardware['hardware_id'] == idToRetrieve:
                results.append(hardware)
        return jsonify(results)
    else:
        return "No Hardware ID provided"


#####################################################
# 3-  CRUD operations for the RESELLER table        #
#####################################################

#=========================================================#
# 3.1. - Implement GET method for all resellers here      #
#=========================================================#
# Endpoint to GET all resellers http://127.0.0.1:5000/api/reseller/all
@app.route('/api/reseller/all', methods=['GET'])
def api_reseller_all():
    # select all reseller_types from DB
    # Add Reseller_ID and use for Update/Delete but never show it on the frontend to user
    select_resellers = """
        SELECT reseller_id, reseller_name,reseller_email,reseller_phone, iso_id
        FROM reseller
        ORDER BY reseller_name ASC; """ 

    resellers = execute_read_query(conn, select_resellers)
    results = [] # List of resulting reseller(s) to return
    for reseller in resellers:
        results.append(reseller)
    return jsonify(results)

#========================================================#
# 3.2 - Implement POST method for reseller here          #
#========================================================#
# Endpoint to ADD an reseller http://127.0.0.1:5000/api/reseller
@app.route('/api/reseller', methods=['POST'])
def add_reseller():
    request_data = request.get_json()
    new_reseller_name = request_data['reseller_name']
    new_reseller_email = request_data['reseller_email']
    new_reseller_phone = request_data['reseller_phone']
    new_iso_id = request_data['iso_id']

    add_reseller_query = """
    INSERT INTO reseller(reseller_name, reseller_email, reseller_phone, iso_id) 
    VALUES('%s', '%s', '%s')""" % (new_reseller_name, new_reseller_email,new_reseller_phone, new_iso_id)
    # print("Insert query is: ", add_reseller_query) // just checking query syntax
    execute_query(conn, add_reseller_query) 
    
    return 'Add request was successful'


#====================================================#
# 3.3 - Implement PUT method for RELELLER here       #
#====================================================#
# Endpoint to UPDATE a reseller http://127.0.0.1:5000/api/reseller (takes a JSON object and update reseller table)
@app.route('/api/reseller', methods=['PUT'])
def update_reseller():
    request_data = request.get_json()
    # reseller data to update 
    idToUpdate = request_data['reseller_id']
    new_reseller_name = request_data['reseller_name']
    new_reseller_email = request_data['reseller_email']
    new_reseller_phone = request_data['reseller_phone']
    new_iso_id = request_data['iso_id']

    update_reseller_query = """
    UPDATE reseller
    SET reseller_name = '%s',
        reseller_email = '%s',
        reseller_phone = '%s',
        iso_id = '%s'
    WHERE reseller_id = %s """ % (new_reseller_name, new_reseller_email,new_reseller_phone, new_iso_id, idToUpdate)
    # print("Update query is: ", update_reseller_query) // just checking query
    execute_query(conn, update_reseller_query)

    return "Update request successful"

#====================================================#
# 3.4 - Implement DELETE method for RESELLER here    #
#====================================================#
# Endpoint to delete an hardware_type http://127.0.0.1:5000/api/hardware?id=x (takes an hardware ID and set isDelete to 'Y')
@app.route('/api/hardware', methods=['DELETE'])
def delete_hardware():
    if 'id' in request.args: # only if an ID is provided as an argument, proceed
        idToDelete = int(request.args['id']) # hardware_type ID to delete 
        delete_hardware_query = """
        DELETE FROM hardware 
        WHERE hardware_id = %s """ % (idToDelete)
        # print("Delete query is: ", delete_hardware_type_query)
        execute_query(conn, delete_hardware_query)
        return "Delete request was successful"
    else:
        return "No hardware ID provided"

#==========================================================#
# 2.5. - Implement GET method for a specific hardware here #
#==========================================================#
# Endpoint to GET all hardware_types http://127.0.0.1:5000/api/hardware?id=x (takes an hardware ID and retrieve it from DB)
@app.route('/api/hardware', methods=['GET'])
def api_hardware_id():
    if 'id' in request.args: # only if an ID is provided as an argument, proceed
        idToRetrieve = int(request.args['id']) # hardware_type ID to Retrieve
        results = [] # List of resulting hardware_type(s) to return
        # Make SELECT only keep ID(s) matching the ID provided
        retrieve_hardware_query = """
        SELECT hardware_id, hardware_name, model_number, htype_id 
        FROM hardware
        WHERE hardware_id = %s ;""" % (idToRetrieve)
        # print("Select query is: ", retrieve_hardware_query) //just checking
        hardwares  = execute_read_query(conn, retrieve_hardware_query)
        for hardware in hardwares:
            if hardware['hardware_id'] == idToRetrieve:
                results.append(hardware)
        return jsonify(results)
    else:
        return "No Hardware ID provided"


# NB: ALWAYS remember to add this line or app won't run
app.run()




#========================================
# Test of all functionalities:          =
#========================================

#   Home page => OK

##### HARDAWRE TYPE ####################
#   api/hardware_type (GET all) =>  OK
#   api/hardware_type (POST = INSERT INTO) => OK
#   api/hardware_type (PUT = UPDATE) => OK
#   api/hardware_type?id=x (Do a physical DELETE for now) => OK
#   api/hardware_type?id=x (GET Hardware Type with id in params)=> OK

##### HARDAWRE  ####################
#   api/hardware (GET all) =>  OK
#   api/hardware(POST = INSERT INTO) => OK
#   api/hardware (PUT = UPDATE) => OK
#   api/hardware?id=x (Do a physical DELETE for now) => OK
#   api/hardware?id=x (GET Hardware with id in params)=> OK