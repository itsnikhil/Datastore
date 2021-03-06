# DataStore

## Introduction

> File-based key-value data store that supports the basic CRD (create, read, and delete) operations. This data store is meant to be used as a local storage for one single process on one laptop.

## Installation

``` pip install pythonfiledatastore ```


## Usage:
    >>> from pythonfiledatastore import datastore_invoke 

#### General Instructions:

    >>> print(datastore_invoke(0))
    Operation Not Found  
    1 for Create (--client --key  --ttl(optional) --value --filepath(optional)) 
    2 for Read (--client --key --filepath(optional)) 
    3 for Delete (--client --key --filepath(optional)) 
    4 for Reset (--client --filepath(optional))

#### Create Operation with file path

    >>> print(datastore_invoke(1, client = "hunch" , key = "employee_data", value = '{"employee":"siam"}', filepath = "/Users/javeed/Desktop/"))
    Create Operation Done

#### Create Operation

    >>> print(datastore_invoke(1, client = "hunch" , key = "employee_data", value = '{"employee":"siam"}'))
    Create Operation Done

#### Create Operation with Time to Live feature

    >>> print(datastore_invoke(1, client = "hunch" , key = "employee_data_temp", value = '{"employee":"ragoish"}', ttl = 30 ))
    Create Operation Done

#### Read Operation

    >>> print(datastore_invoke(2, client = "hunch" , key = "employee_data"))
    For key | employee_data | value  - {'employee': 'siam'} 

#### Read Operation TTL Expired 

    >>> print(datastore_invoke(2, client = "hunch" , key = "employee_data_temp"))
    Error Status : TTL Value for the Key - employee_data_temp expired for the client - hunch

#### Delete Operation 

    >>> print(datastore_invoke(3, client = "hunch" , key = "employee_data"))
    Error Status : For key | employee_data | value - is deleted

#### Delete Operation TTL Expired

    >>> print(datastore_invoke(3, client = "hunch" , key = "employee_data_temp"))
    Error Status : TTL Value for the Key - employee_data_temp expired for the client - hunch

> Note: After Delete Option if the client storage file is empty, A forced reset operation is performed

#### Reset Operation - Delete Entire file

    >>> print(datastore_invoke(4, client = "hunch" ))
    File removed!!!! - hunch
