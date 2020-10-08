import boto3

def get_resource():
    return boto3.resource('s3', **credentials)

def get_client():
    return boto3.client('s3', **credentials)

def list_buckets():

    resource = get_resource()
    for bucket in resource.buckets.all():
        print (bucket.name)

    return bucket.name

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

    '''
    print (response)
    print ()
    print (response['ContentLength'])

    for key in response:
        print (key + ': ' + str( response[key]))
        print ()
    '''

    return bytes_to_giga( response['ContentLength'] )

def add_s3n_to_key(key):

    return 's3n://' + key

def bytes_to_giga(bytes):

    return bytes / 1024 / 1024 / 1024

def import_credentials(file_path, export_role, set_creds = True):

    file = open(file_path, 'r')

    roles = {}

    for i in file.readlines():
        i = i.strip()

        kv = i.split('=')

        if len(kv) == 1:
            #it is a role
            role = kv[0][1:-1]

            if role == '':
                continue

            roles[role] = {}

        else:
            roles[role].update(  {kv[0].strip() : kv[1].strip() }  )

    if set_creds:
        set_credentials(roles[export_role])

    file.close()

    return roles[export_role]

def set_credentials(dictionary):

    global credentials
    credentials = dictionary
