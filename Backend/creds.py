#=======================================================
# Use these creds for all connection to our AWS DEV DB #
#=======================================================

class Creds:
    conString = 'ovvidbinstance.c9rwb1hk6i86.us-east-1.rds.amazonaws.com'
    userName = 'OvviDBA'
    password = 'OvviAdmin2023'
    dbName = 'OvviDevDB' 

    


#========================================================
# Change to Prod DB info. once DEV TESTS are done       #
# Just uncomment next block and comment previous one    #
#========================================================

"""
class Creds:
    conString = 'rds-mysql-ovviproject.cqw9wvzdacxo.us-east-1.rds.amazonaws.com'
    userName = 'admin'
    password = 'Ovvi!123'
    dbName = 'ovvi' 
"""