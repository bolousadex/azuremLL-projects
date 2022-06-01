
# -----------------------------------------------------
# Import required classes from Azureml
# -----------------------------------------------------
from azureml.core import Workspace, Datastore, Dataset, Experiment


# -----------------------------------------------------
# Access the Workspace, Datastore and Datasets
# -----------------------------------------------------
ws                = ws = Workspace.from_config("./config")
az_store          = Datastore.get(ws, 'mystore1')
az_dataset        = Dataset.get_by_name(ws, 'myloanapplication')
az_default_store  = ws.get_default_datastore()

# -----------------------------------------------------
# Create/Access an experiment object
# -----------------------------------------------------
experiment = Experiment(workspace=ws,
                        name="Loan-SDK-Exp01")


# -----------------------------------------------------
# Run an experiment using start_logging method
# -----------------------------------------------------
new_run = experiment.start_logging()


# -----------------------------------------------------
# Do your stuff here
# -----------------------------------------------------
df = az_store.to_pandas_dataframe()

# Count the observations
total_observations = len(df)

# Get the null/missing values
nulldf = df.isnull().sum()


# -----------------------------------------------------
# Log metrics and Complete an experiment run
# -----------------------------------------------------

# Log the metrics to the workspace
new_run.log("Total Observations", total_observations)

# Log the missing data values
for columns in df.columns:
    new_run.log(columns, nulldf[columns])

new_run.complete()

