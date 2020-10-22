#import the s3_funcs module
import s3_funcs


credentials_path = 'C:/Users/e150445/Desktop/aws_creds.txt'
aws_role = '721818040399_aap-datasci-ic-stl'

credentials = s3_funcs.import_credentials(credentials_path, aws_role)

bucket = 'aa-userland-s3-nonprd'
prefix = 'datalabs/ic-stl/shared/DATA_EXTRACTS_METER_DATA/'

s3_funcs.list_files(bucket, prefix)
