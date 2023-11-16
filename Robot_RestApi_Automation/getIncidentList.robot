*** Settings ***
Library    SeleniumLibrary
Library    RequestsLibrary
Library    JsonLibrary
Library    Collections

*** Test Cases ***
Get incidents list from servicenow
    [Documentation]     Get all incidents
    [Tags]     smoke
    Create Session    mysession    https://dev176532.service-now.com     verify=${True}
    ${response} = Get On Session  mysession /api/now/table/incident/   params=query=assignment_group=d625dccec0a8016700a222a0f7900d06
    Status Should Be    200    ${response}

    