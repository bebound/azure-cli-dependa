# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps

# pylint: disable=line-too-long

helps['logicapp'] = """
type: group
short-summary: Manage logic apps.
"""

helps['logicapp create'] = """
type: command
short-summary: Create a logic app.
long-summary: The logic app's name must be able to produce a unique FQDN as AppName.azurewebsites.net.
examples:
  - name: Create a basic logic app.
    text: >
        az logicapp create -g myRG --subscription mySubscription -p MyPlan -n myLogicApp -s myStorageAccount
"""

helps['logicapp delete'] = """
type: command
short-summary: Delete a logic app.
examples:
  - name: Delete a logic app.
    text: az logicapp delete --name myLogicApp --resource-group myRG --subscription mySubscription
"""

helps['logicapp show'] = """
type: command
short-summary: Get the details of a logic app.
examples:
  - name: Get the details of a logic app.
    text: az logicapp show --name myLogicApp --resource-group myRG --subscription mySubscription
"""

helps['logicapp list'] = """
type: command
short-summary: List logic apps.
examples:
  - name: List default host name and state for all logic apps.
    text: >
        az logicapp list --query "[].hostName: defaultHostName, state: state"
  - name: List all running logic apps.
    text: >
        az logicapp list --query "[?state=='Running']"
"""

helps['logicapp restart'] = """
type: command
short-summary: Restart a logic app.
examples:
  - name: Restart a logic app.
    text: az logicapp restart --name myLogicApp --resource-group myRG
    crafted: true
"""

helps['logicapp start'] = """
type: command
short-summary: Start a logic app.
examples:
  - name: Start a logic app
    text: az logicapp start --name myLogicApp --resource-group myRG
    crafted: true
"""

helps['logicapp stop'] = """
type: command
short-summary: Stop a logic app.
examples:
  - name: Stop a logic app.
    text: az logicapp stop --name myLogicApp --resource-group myRG
    crafted: true
"""

helps['logicapp deployment'] = """
type: group
short-summary: Manage logic app deployments.
"""

helps['logicapp deployment source'] = """
type: group
short-summary: Manage logicapp app deployment via source control.
"""

helps['logicapp deployment source config-zip'] = """
type: command
short-summary: Perform deployment using the kudu zip push deployment for a logic app.
examples:
  - name: Perform deployment by using zip file content.
    text: >
        az logicapp deployment source config-zip \\
            -g myRG -n myLogicApp --subscription mySubscription \\
            --src zipFilePathLocation
"""

helps['logicapp scale'] = """
type: command
short-summary: Scale a logic app.
examples:
  - name: Scale a logic app.
    text: az logicapp scale --name myLogicApp --resource-group myRG --subscription mySubscription --min-instances 2 --max-instances 4
    crafted: true
"""

helps['logicapp config'] = """
type: group
short-summary: Configure a logic app.
"""

helps['logicapp config appsettings'] = """
type: group
short-summary: Configure logic app settings.
"""

helps['logicapp config appsettings delete'] = """
type: command
short-summary: Delete a logic app's settings.
long-summary: Note that setting values are now redacted in the result. Please use the `az logicapp config appsettings list` command to view the settings.
examples:
  - name: Delete a logic app's settings. (autogenerated)
    text: az logicapp config appsettings delete --name myLogicApp --resource-group myRG --subscription mySubscription --setting-names setting-names
    crafted: true
"""

helps['logicapp config appsettings list'] = """
type: command
short-summary: Show settings for a logic app.
examples:
  - name: Show settings for a logic app. (autogenerated)
    text: az logicapp config appsettings list --name myLogicApp --resource-group myRG --subscription mySubscription
    crafted: true
"""

helps['logicapp config appsettings set'] = """
type: command
short-summary: Update a logic app's settings.
long-summary: Note that setting values are now redacted in the result. Please use the `az logicapp config appsettings list` command to view the settings.
examples:
  - name: Update a logic app's settings.
    text: |
        az logicapp config appsettings set --name myLogicApp --resource-group myRG --subscription mySubscription --settings "AzureWebJobsStorage=$storageConnectionString"
"""

helps['logicapp update'] = """
type: command
short-summary: Update a logic app.
examples:
  - name: Update a logic app. (autogenerated)
    text: az logicapp update --name myLogicApp --resource-group myRG
    crafted: true
"""
