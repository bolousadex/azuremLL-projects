from azureml.core.authentication import InteractiveLoginAuthentication
from azureml.core import Workspace, Experiment, ScriptRunConfig, Datastore, Dataset
from azureml.core import Run

# create the workspace
ia = InteractiveLoginAuthentication(
    tenant_id='04249128-062f-48b9-8bd2-44cc89c911fa')
ws = Workspace.create(name='boluazureshow',
                      subscription_id='b0feb439-94a6-4da8-a478-6c12cf49ad44',
                      resource_group='my_new_experiment',
                      create_resource_group=False, auth=ia,   # True if it does not exist
                      location='East US')

# create the datastore
ds = Datastore.register_azure_blob_container(workspace=ws, datastore_name="mystore1", container_name="mystorenow", account_name="loandata",
                                             account_key="Pq4fGNqR77mVio96TRQQonQR7emz/GSMlohXqxxz9sOiGzBbX6EFuGdCxGGaHKIeYCI7VfVZBtLW+AStN+Aj+g==")
ws = Workspace.from_config(path="./config")
az_store = Datastore.get(ws, "mystore1")

# create the path
datapath = [(az_store,"C:/Users/admin/Desktop/personal/analytics special/azure ml cheat sheet/Loan+Approval+Prediction.csv")]

# create dataset

loan_dataset = Dataset.from_delimited_files(
    path="C:/Users/admin/Desktop/personal/analytics special/azure ml cheat sheet/Loan+Approval+Prediction.csv")

# Register dataset
loan_dataset = loan_dataset.register(workspace=ws, name="myloanapplication",
                                     if_exist=True)
