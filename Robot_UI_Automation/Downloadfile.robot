
*** Settings ***
Library    SeleniumLibrary
Library    SNrequestitemdetails.py
Library    RPA.Robocorp.WorkItems

*** Variables ***
${URL}        https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${BROWSER}    Chrome

*** Keywords ***
download file
    &{value}    SNrequestitemdetails.Getrequestitemdesc
    FOR    ${element_val}    IN    @{value.values()}
        IF    '${element_val}' == "Galaxy"
            LoginToApplication
        END
        IF    '${element_val}' == "Retina"
            Log To Console    RetinaReport
        END
        IF    '${element_val}' == "S7"
            Log To Console    S7Report
        END
        IF    '${element_val}' == "Lenovo"
            Log To Console    LenovoReport
        END     
    END   

LoginToApplication
    Open Browser     ${URL}     ${BROWSER}
    Maximize Browser Window
    Sleep    5
    Input Text    username    admin
    Input Password    password    admin123
    Click Button    xpath://button[@class = 'oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']
    Sleep    10s
    Log To Console    User log succesful