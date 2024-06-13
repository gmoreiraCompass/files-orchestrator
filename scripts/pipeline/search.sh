bucket_name=$1
aws_key=$2
aws_access_key=$3
aws_access_secret=$4
local_path=$5

echo "VARIABLES"
echo "1 - "$bucket_name
echo "2 - "$aws_key
echo "3 - "$aws_access_key
echo "4 - "$aws_access_secret
echo "5 - "$local_path

# Install required dependencies for Python script
pip3 install boto3 pathlib

# Run upload script
python3 scripts/pipeline/search_documents.py $bucket_name $aws_key $aws_access_key $aws_access_secret $local_path