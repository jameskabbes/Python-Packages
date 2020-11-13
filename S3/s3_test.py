#import the s3_funcs module
import s3_funcs
import sys

### Update with your own location

aws_creds_folder = 'C:/Users/e150445/Documents/AWS-Credentials'
sys.path.append( aws_creds_folder )
import import_credentials as imp_cred

credentials_path = aws_creds_folder + '/' + 'aws_creds.txt'
aws_role = '721818040399_aap-s3temp-ic-uiuc'

###import credentials
creds = s3_funcs.import_credentials( credentials_path,  aws_role )
print (creds)

### Insert your own s3_functions to test
s3_funcs.list_buckets()

bucket = 'aee-analytics-tools-dev-in-il'
s3_funcs.list_files( bucket, 'AIM_Sample_Data/')
s3_funcs.list_subfolders( bucket, '')
