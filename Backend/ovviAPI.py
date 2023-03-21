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
        idToRetrieve = int(request.args['id']) # hardware ID to Retrieve
        results = [] # List of resulting hardware(s) to return
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
    VALUES('%s', '%s', '%s', '%s')""" % (new_reseller_name, new_reseller_email,new_reseller_phone, new_iso_id)
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
# Endpoint to delete an reseller http://127.0.0.1:5000/api/reseller?id=x (takes an reseller ID and delete record)
@app.route('/api/reseller', methods=['DELETE'])
def delete_reseller():
    if 'id' in request.args: # only if an ID is provided as an argument, proceed
        idToDelete = int(request.args['id']) # reseller ID to delete 
        delete_reseller_query = """
        DELETE FROM reseller 
        WHERE reseller_id = %s """ % (idToDelete)
        # print("Delete query is: ", delete_reseller_query)
        execute_query(conn, delete_reseller_query)
        return "Delete request was successful"
    else:
        return "No reseller ID provided"

#==========================================================#
# 3.5. - Implement GET method for a specific reseller here #
#==========================================================#
# Endpoint to GET all resellers http://127.0.0.1:5000/api/reseller?id=x (takes a reseller ID and retrieve it from DB)
@app.route('/api/reseller', methods=['GET'])
def api_reseller_id():
    if 'id' in request.args: # only if an ID is provided as an argument, proceed
        idToRetrieve = int(request.args['id']) # reseller_type ID to Retrieve
        results = [] # List of resulting reseller(s) to return
        # Make SELECT only keep ID(s) matching the ID provided
        retrieve_reseller_query = """
        SELECT reseller_id, reseller_name, reseller_email, reseller_phone, iso_id 
        FROM reseller
        WHERE reseller_id = %s ;""" % (idToRetrieve)
        # print("Select query is: ", retrieve_reseller_query) //just checking
        resellers  = execute_read_query(conn, retrieve_reseller_query)
        for reseller in resellers:
            if reseller['reseller_id'] == idToRetrieve:
                results.append(reseller)
        return jsonify(results)
    else:
        return "No reseller ID provided"

######################################################
# 4 -  CRUD operations for the ISO table     #
######################################################

#=========================================================#
# 4.1. - Implement GET method for all ISO here #
#=========================================================#
# Endpoint to GET iso http://127.0.0.1:5000/api/iso/all
@app.route('/api/iso/all', methods=['GET'])
def api_iso_all():
    select_iso = """
        SELECT *
        FROM iso;  """ 

    iso_results = execute_read_query(conn, select_iso)
    results = [] 
    for iso in iso_results:
        results.append(iso)
    return jsonify(results)

#========================================================#
# 4.2 - Implement POST method for ISO here     #
#========================================================#
# Endpoint to ADD an ISO http://127.0.0.1:5000/api/iso
@app.route('/api/iso', methods=['POST'])
def add_iso():
    request_data = request.get_json()
    new_iso_company = request_data['ISO_COMPANY']
    
    add_iso_query = """
    INSERT INTO iso(ISO_COMPANY) 
    VALUES('%s')""" % (new_iso_company)
    execute_query(conn, add_iso_query) 
    
    return 'Add request was successful'


#====================================================#
# 4.3 - Implement PUT method for ISO here     #
#====================================================#
# Endpoint to UPDATE an ISO http://127.0.0.1:5000/api/iso (takes a JSON object and update iso table)
@app.route('/api/iso', methods=['PUT'])
def update_iso():
    request_data = request.get_json()

    idToUpdate = request_data['iso_id']
    new_iso_company = request_data['iso_company']
    update_iso_query = """
    UPDATE iso
    SET ISO_COMPANY = '%s'  
    WHERE ISO_ID = %s """ % (new_iso_company, idToUpdate)
    execute_query(conn, update_iso_query)

    return "Update request successful"

#====================================================#
# 4.4 - Implement DELETE method for ISO here   #
#====================================================#
# Endpoint to delete an iso http://127.0.0.1:5000/api/iso?id=x (takes an iso ID)
@app.route('/api/iso', methods=['DELETE'])
def delete_iso():
    if 'id' in request.args: # only if an ID is provided as an argument, proceed
        idToDelete = int(request.args['id']) # hardware_type ID to delete 
        delete_iso_query = """
        DELETE FROM iso 
        WHERE iso_id = %s """ % (idToDelete)
        execute_query(conn, delete_iso_query)
        return "Delete request was successful"
    else:
        return "No ISO ID provided"


#===============================================================#
# 4.5. - Implement GET method for a specific ISO here #
#===============================================================#
# Endpoint to GET a specific ISO company http://127.0.0.1:5000/api/iso?id=x (takes an iso ID and retrieve it from DB)
@app.route('/api/iso', methods=['GET'])
def api_iso_id():
    if 'id' in request.args: # only if an ID is provided as an argument, proceed
        idToRetrieve = int(request.args['id']) # iso ID to Retrieve
        results = [] # List of resulting iso(s) to return
        retrieve_iso_query = """
        SELECT *
        FROM iso
        WHERE ISO_ID = %s; """ % (idToRetrieve)
        iso_query = execute_read_query(conn, retrieve_iso_query)
        for iso in iso_query:
            if iso['ISO_ID'] == idToRetrieve:
                results.append(iso)
        return jsonify(results)
    else:
        return "No ISO ID provided"

######################################################
# 5 -  CRUD operations for the MERCHANT table     #
######################################################

#=========================================================#
# 5.1. - Implement GET method for all MERCHANTS here #
#=========================================================#
# Endpoint to GET all merchants http://127.0.0.1:5000/api/merchant/all
@app.route('/api/merchant/all', methods=['GET'])
def api_merchant_all():
    select_merchant_query = """
    SELECT merchant_id, merchant_name,merchant_address1,merchant_address2,merchant_city,merchant_state,merchant_zip,merchant_email,merchant_phone,reseller_id
    FROM merchant; """

    merchants = execute_read_query(conn, select_merchant_query)
    results = [] # List of resulting merchant(s) to return
    print(results)
    for merchant in merchants:
        results.append(merchant)
    return jsonify(results)

#========================================================#
# 5.2 - Implement POST method for MERCHANT table here     #
#========================================================#
# Endpoint to ADD a merchant http://127.0.0.1:5000/api/merchant

# Check if Josh corrected "request.data" on all Merchant CRUD Ops and pull from origin
@app.route('/api/merchant', methods=['POST'])
def add_merchant():
    request_data = request.get_json()
    new_merchant_name = request_data['merchant_name']
    new_merchant_address1 = request_data['merchant_address1']
    new_merchant_address2 = request_data['merchant_address2']
    new_merchant_city = request_data['merchant_city']
    new_merchant_state = request_data['merchant_state']
    new_merchant_zip = request_data['merchant_zip']
    new_merchant_email = request_data['merchant_email']
    new_merchant_phone = request_data['merchant_phone']
    foreign_reseller_id = request_data['reseller_id']
    
    add_merchant_query = """
    INSERT INTO merchant(merchant_name,merchant_address1,merchant_address2,merchant_city,merchant_state,merchant_zip,merchant_email,merchant_phone,reseller_id) 
    VALUES('%s','%s','%s','%s','%s',%s,'%s',%s,%s)""" % (new_merchant_name,new_merchant_address1,new_merchant_address2,new_merchant_city,new_merchant_state,new_merchant_zip,
    new_merchant_email,new_merchant_phone,foreign_reseller_id)
    #print("Insert query is: ", add_merchant_query) # just checking query syntax
    execute_query(conn, add_merchant_query) 
    
    return 'Add request was successful'


#====================================================#
# 5.3 - Implement PUT method for MERCHANT here     #
#====================================================#
# Endpoint to UPDATE a merchant http://127.0.0.1:5000/api/merchant (takes a JSON object and update merchant table)
@app.route('/api/merchant', methods=['PUT'])
def update_merchant():
    request_data = request.get_json()
    idToUpdate = request_data['merchant_id']
    new_merchant_name = request_data['merchant_name']
    new_merchant_address1 = request_data['merchant_address1']
    new_merchant_address2 = request_data['merchant_address2']
    new_merchant_city = request_data['merchant_city']
    new_merchant_state = request_data['merchant_state']
    new_merchant_zip = request_data['merchant_zip']
    new_merchant_email = request_data['merchant_email']
    new_merchant_phone = request_data['merchant_phone']
    foreign_reseller_id = request_data['reseller_id']

    
    update_merchant_query = """
    UPDATE merchant
    SET merchant_name = '%s',
    merchant_address1 = '%s',
    merchant_address2 = '%s',
    merchant_city = '%s',
    merchant_state = '%s',
    merchant_zip = %s,
    merchant_email = '%s',
    merchant_phone = %s,
    reseller_id = %s   
    WHERE merchant_id = %s """ % (new_merchant_name,new_merchant_address1,new_merchant_address2,new_merchant_city,new_merchant_state,new_merchant_zip,
    new_merchant_email,new_merchant_phone,foreign_reseller_id,idToUpdate)
    #print("Update query is: ", update_merchant_query) # just checking query
    execute_query(conn, update_merchant_query)

    return "Update request successful"

#====================================================#
# 5.4 - Implement DELETE method for MERCHANT here   #
#====================================================#
# Endpoint to delete a merchant http://127.0.0.1:5000/api/merchant?id=x (takes a merchant ID and set isDelete to 'Y')
@app.route('/api/merchant', methods=['DELETE'])
def delete_merchant():
    if 'id' in request.args: # only if an ID is provided as an argument, proceed
        idToDelete = int(request.args['id']) # merchant ID to delete 
        delete_merchant_query = """
        DELETE FROM merchant 
        WHERE merchant_id = %s """ % (idToDelete)
        execute_query(conn, delete_merchant_query)
        return "Delete request was successful"
    else:
        return "No merchant ID provided"


#===============================================================#
# 5.5. - Implement GET method for a specific MERCHANT here #
#===============================================================#
# Endpoint to GET a specific merchant http://127.0.0.1:5000/api/merchant?id=x (takes a merchant ID and retrieve it from DB)
@app.route('/api/merchant', methods=['GET'])
def api_merchant_id():
    if 'id' in request.args: # only if an ID is provided as an argument, proceed
        idToRetrieve = int(request.args['id']) # hardware_type ID to Retrieve
        retrieve_merchant_query = """
        SELECT merchant_id, merchant_name,merchant_address1,merchant_address2,merchant_city,merchant_state,merchant_zip,merchant_email,merchant_phone,reseller_id 
        FROM merchant
        WHERE merchant_id = %s; """ % (idToRetrieve)
        merchants  = execute_read_query(conn, retrieve_merchant_query)
        results = []
        for merchant in merchants:
            #print(info)
            if merchant['merchant_id'] == idToRetrieve:
                results.append(merchant)
        return jsonify(results)
    else:
        return "No merchant ID provided"

######################################################
# 6 -  CRUD operations for the ORDERS table          #
######################################################

#=========================================================#
# 6.1. - Implement GET method for all Orders here         #
#=========================================================#
# Endpoint to GET all orders http://127.0.0.1:5000/api/orders/all
@app.route('/api/orders/all', methods=['GET'])
def api_orders_all():
    select_orders = """
        SELECT *
        FROM orders;  """ 

    order_results = execute_read_query(conn, select_orders)
    results = [] 
    for order in order_results:
        results.append(order)
    return jsonify(results)

#========================================================#
# 6.2 - Implement POST method for Orders here            #
#========================================================#
# Endpoint to ADD an Order http://127.0.0.1:5000/api/orders
@app.route('/api/orders', methods=['POST'])
def add_order():
    request_data = request.get_json()
    new_order_number = request_data['order_num']
    new_serial_number = request_data['serial_number']
    new_tracking_num = request_data['tracking_num']
    new_order_date = request_data['order_date']
    new_ship_date = request_data['ship_date']
    new_hardware_id = request_data['hardware_id']
    new_merchant_id = request_data['merchant_id']
    
    add_orders_query = """
    INSERT INTO orders(order_num,serial_number,tracking_num,order_date,ship_date,hardware_id,merchant_id) 
    VALUES(%s, '%s','%s','%s','%s',%s,%s);""" % (new_order_number, new_serial_number,new_tracking_num,new_order_date,new_ship_date,new_hardware_id,new_merchant_id)
    execute_query(conn, add_orders_query) 
    
    return 'Add request was successful'


#====================================================#
# 6.3 - Implement PUT method for Orders here     #
#====================================================#
# Endpoint to UPDATE an Order http://127.0.0.1:5000/api/orders (takes a JSON object and update orders table)
@app.route('/api/orders', methods=['PUT'])
def update_order():
    request_data = request.get_json()

    idToUpdate = request_data['order_id']
    new_order_number = request_data['order_num']
    new_serial_number = request_data['serial_number']
    new_tracking_num = request_data['tracking_num']
    new_order_date = request_data['order_date']
    new_ship_date = request_data['ship_date']
    new_hardware_id = request_data['hardware_id']
    new_merchant_id = request_data['merchant_id']
    
    update_orders_query = """
    UPDATE orders
    SET order_num = %s,
    serial_number = '%s',
    tracking_num = '%s',
    order_date = '%s',
    ship_date = '%s',
    hardware_id = %s,
    merchant_id = %s  
    WHERE order_id = %s """ % (new_order_number, new_serial_number,new_tracking_num,new_order_date,new_ship_date,new_hardware_id,new_merchant_id,idToUpdate)
    execute_query(conn, update_orders_query)

    return "Update request successful"

#====================================================#
# 6.4 - Implement DELETE method for Orders here   #
#====================================================#
# Endpoint to delete an Order http://127.0.0.1:5000/api/orders?id=x (takes an order_ID)
@app.route('/api/orders', methods=['DELETE'])
def delete_order():
    if 'id' in request.args: # only if an ID is provided as an argument, proceed
        idToDelete = int(request.args['id']) # ORDER_ID to delete 
        delete_order_query = """
        DELETE FROM orders 
        WHERE order_id = %s """ % (idToDelete)
        execute_query(conn, delete_order_query)
        return "Delete request was successful"
    else:
        return "No ORDER_ID provided"


#===============================================================#
# 6.5. - Implement GET method for a specific Orders here #
#===============================================================#
# Endpoint to GET specific Orders http://127.0.0.1:5000/api/orders?id=x (takes an ORDER_ID and retrieve it from DB)
@app.route('/api/orders', methods=['GET'])
def api_order_id():
    if 'id' in request.args: # only if an ID is provided as an argument, proceed
        idToRetrieve = int(request.args['id']) # ORDER_ID to Retrieve
        results = [] # List of resulting order(s) to return
        retrieve_order_query = """
        SELECT order_id, order_num,serial_number,tracking_num,order_date,ship_date,hardware_id,merchant_id
        FROM orders
        WHERE order_id = %s; """ % (idToRetrieve)
        orders = execute_read_query(conn, retrieve_order_query)
        for order in orders:
            if order['order_id'] == idToRetrieve:
                results.append(order)
        return jsonify(results)
    else:
        return "No ORDER_ID provided"

######################################################
# 7 - Reports JSON Operations                   #
######################################################

#===============================================================#
# 7.1 - Viewing an ISO you should be able to view the resellers within them and their contact information #
#===============================================================#
# Endpoint is http://127.0.0.1:5000/api/SevenOne?id=x
@app.route('/api/SevenOne', methods=['GET'])
def api_seven_one():
    if 'id' in request.args: # only if an ID is provided as an argument, proceed
        idToRetrieve = int(request.args['id']) 
        seven_one_query = """
        SELECT iso.ISO_COMPANY as "ISO Company", reseller.RESELLER_ID as "Reseller ID",
        reseller.RESELLER_NAME as "Reseller Name", reseller.RESELLER_EMAIL as "Reseller Email", reseller.RESELLER_PHONE as "Reseller Phone Number"
        FROM iso
        JOIN reseller
        ON iso.ISO_ID = reseller.ISO_ID
        WHERE iso.ISO_ID = %s; """ % (idToRetrieve)
        results  = execute_read_query(conn, seven_one_query)
        return jsonify(results)
    else:
        return "No ISO ID provided"

#===============================================================#
# 7.2 - Viewing a Reseller you should get all their information as well as what ISO they are under #
#===============================================================#
# Endpoint is http://127.0.0.1:5000/api/SevenTwo?id=x
@app.route('/api/SevenTwo', methods=['GET'])
def api_seven_two():
    if 'id' in request.args: # only if an ID is provided as an argument, proceed
        idToRetrieve = int(request.args['id']) 
        seven_two_query = """
        SELECT iso.ISO_COMPANY as "ISO Company", iso.ISO_ID as "ISO ID", reseller.RESELLER_ID as "Reseller ID",
        reseller.RESELLER_NAME as "Name", reseller.RESELLER_EMAIL as "Email", reseller.RESELLER_PHONE as "Phone Number"
        FROM reseller
        JOIN iso
        ON reseller.ISO_ID = iso.ISO_ID
        WHERE reseller.RESELLER_ID = %s; """ % (idToRetrieve)
        results  = execute_read_query(conn, seven_two_query)
        return jsonify(results)
    else:
        return "No ISO ID provided"

#===============================================================#
# 7.3 - Should have another view that shows all merchants attached to a reseller with contact info #
#===============================================================#
# Endpoint is http://127.0.0.1:5000/api/SevenThree?id=x
@app.route('/api/SevenThree', methods=['GET'])
def api_seven_three():
    if 'id' in request.args: # only if an ID is provided as an argument, proceed
        idToRetrieve = int(request.args['id']) 
        seven_three_query = """
        SELECT reseller.RESELLER_ID as "Reseller ID", reseller.RESELLER_NAME as "Reseller Name", reseller.RESELLER_EMAIL as "Reseller Email",
        reseller.RESELLER_PHONE as "Reseller Phone", merchant.MERCHANT_ID as "Merchant ID", merchant.MERCHANT_NAME as "Merchant Name",
        CONCAT_WS(', ',merchant.MERCHANT_ADDRESS1, merchant.MERCHANT_ADDRESS2, merchant.MERCHANT_CITY, merchant.MERCHANT_STATE, merchant.MERCHANT_ZIP)
        as "Merchant Address", merchant.MERCHANT_EMAIL as "Merchant Email", merchant.MERCHANT_PHONE as "Merchant Phone"
        FROM reseller
        JOIN merchant
        ON reseller.RESELLER_ID = merchant.RESELLER_ID
        WHERE reseller.RESELLER_ID = %s; """ % (idToRetrieve)
        results  = execute_read_query(conn, seven_three_query)
        return jsonify(results)
    else:
        return "No Reseller ID provided"

# NB: ALWAYS remember to add this line or app won't run
app.run()




#========================================
# Test of all functionalities:          =
#========================================

#   Home page => OK

##### 1. HARDAWRE TYPE ####################
#   api/hardware_type (GET all) =>  OK
#   api/hardware_type (POST = INSERT INTO) => OK
#   api/hardware_type (PUT = UPDATE) => OK
#   api/hardware_type?id=x (Do a physical DELETE for now) => OK
#   api/hardware_type?id=x (GET Hardware Type with id in params)=> OK

##### 2. HARDWARE  ####################
#   api/hardware (GET all) =>  OK
#   api/hardware(POST = INSERT INTO) => OK
#   api/hardware (PUT = UPDATE) => OK
#   api/hardware?id=x (Do a physical DELETE for now) => OK
#   api/hardware?id=x (GET Hardware with id in params)=> OK

##### 3. RESELLER  ####################
#   api/reseller (GET all) =>  OK
#   api/reseller(POST = INSERT INTO) => OK
#   api/reseller (PUT = UPDATE) => OK
#   api/reseller?id=x (Do a physical DELETE for now) => OK
#   api/reseller?id=x (GET reseller with id in params)=> OK

##### 4. ISO  ####################
#   api/iso (GET all) =>  OK
#   api/iso(POST = INSERT INTO) => OK
#   api/iso (PUT = UPDATE) => OK
#   api/iso?id=x (Do a physical DELETE for now) => OK
#   api/iso?id=x (GET iso with id in params)=> OK

##### 5. MERCHANT  ####################
#   api/merchant (GET all) => OK
#   api/merchant(POST = INSERT INTO) => OK, Needs Error Detection.
#   api/merchant (PUT = UPDATE) => OK
#   api/merchant?id=x (Do a physical DELETE for now) => OK
#   api/merchant?id=x (GET merchant with id in params)=> OK

##### 6. ORDERS  ####################
#   api/orders (GET all) => 
#   api/orders(POST = INSERT INTO) => OK
#   api/orders (PUT = UPDATE) => OK
#   api/orders?id=x (Do a physical DELETE for now) => OK
#   api/orders?id=x (GET merchant with id in params)=> OK