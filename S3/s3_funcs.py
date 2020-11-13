import boto3

def get_resource():
    return boto3.resource('s3', **credentials)

def get_client():
    return boto3.client('s3', **credentials)

def list_buckets():

    resource = get_resource()
    buckets = []
    for bucket in resource.buckets.all():
        print (bucket.name)
        buckets.append(bucket.name)

    return buckets

def list_subfolders(bucket, prefix):

    #prefix needs to end with a /
    if len(prefix) > 0:
        assert prefix[-1] =='/'

    client = get_client()
    result = client.list_objects(Bucket=bucket, Prefix=prefix, Delimiter='/')

    subfolders = []

    try:
        for i in result.get('CommonPrefixes'):
            print ('subfolder : ', i.get('Prefix'))
            subfolders.append(i.get('Prefix'))
    except:
        print ('No subfolders')

    return subfolders

def list_files(bucket, prefix):

    client = get_client()
    response = client.list_objects_v2(Bucket = bucket, Prefix = prefix)

    filenames = []
    for file_dict in response['Contents']:
        filenames.append(file_dict['Key'])

    for i in range(len(filenames)):
        print (str(i+1) + '. ' + str(filenames[i]))

    print()
    print ('Found ' + str(len(filenames)) + ' files')
    return filenames

def get_file_from_key(key):

    return key.split('/')[-1]

def upload_file(bucket, key, filename):

    #key is the entire aws path
    #filename is the base path of the file

    resource = get_resource()
    resource.meta.client.upload_file(filename, bucket, key)

def download_file(bucket, key, filename):

    #key is the entire aws path
    #filename is the base path of the file
    resource = get_resource()
    resource.meta.client.download_file(bucket, key, filename)

def get_total_size_of_subfolder(bucket, prefix):

    files = list_files(bucket, prefix)

    total = 0

    for file in files:
        total += get_file_size(bucket, file)

    print ()
    print ()
    print ('Total: ' + str(total) + ' GB')

    return total

def get_file_size(bucket, key):

    client = get_client()
    response = client.head_object(Bucket = bucket, Key = key)

    return bytes_to_giga( response['ContentLength'] )

def add_s3n_to_key(key):

    #testing github
    return 's3n://' + key

def bytes_to_giga(bytes):

    return bytes / 1024 / 1024 / 1024

def import_all_roles( credentials_path ):

    ###Set Filename
    file = open(  credentials_path , 'r')

    ###Find which roles are contained in the file
    roles = {}

    for line in file.readlines():
        line = line.strip()

        if line[0] == '[' and line[-1] == ']':
            #this is a role
            role = line[1:-1]
            roles[role] = {}

        elif line == '':
            #blank lines
            continue

        else:
            #should be a key-value combo
            key_value_list = line.split('=')

            if len(key_value_list) != 1:

                for i in range(len(line)):
                    if line[i] == '=':
                        #find the first instance of an equal sign

                        key = line[:i].strip()
                        value = line[(i+1):].strip()
                        break

                roles[role].update( {key : value} )


    file.close()

    return roles

def import_role(credentials_path, role):

    roles = import_all_roles(credentials_path)

    for role_id in roles:
        if role in role_id:
            return roles[ role_id ]

def import_credentials(file_path, export_role, set_creds = True):

    '''File path is a text file that looks like this

    ///Begin File
    [721818040399_aap-datasci-ic-stl]
    aws_access_key_id = ABCDEFGHIJKLM
    aws_secret_access_key = ABCDEFGHIJKLM
    aws_session_token = ABCDEFGHIJKLM

    [721818040399_aap-datasci-ic-uiuc]
    aws_access_key_id = ABCDEFGHIJKLM
    aws_secret_access_key = ABCDEFGHIJKLM
    aws_session_token = ABCDEFGHIJKLM

    [721818040399_aap-s3temp-ic-uiuc]
    aws_access_key_id = ABCDEFGHIJKLM
    aws_secret_access_key = ABCDEFGHIJKLM
    aws_session_token = ABCDEFGHIJKLM
    ///End File

    ^^^Export role is one of the three
    1. '721818040399_aap-datasci-ic-stl'
    2. '721818040399_aap-datasci-ic-uiuc'
    3. '721818040399_aap-s3temp-ic-uiuc'
    '''
    role_dict = import_role(file_path, export_role)

    if set_creds:
        set_credentials( role_dict )

    return role_dict

def set_credentials(dictionary):

    global credentials
    credentials = dictionary
