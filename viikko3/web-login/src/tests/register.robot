*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  testi
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  mo
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Fail With Message  Username is too short


Register With Valid Username And Invalid Password
    Set Username  kalle
    Set Password  password
    Set Password Confirmation  password
    Submit Credentials
    Register Should Fail With Message  Password cannot contain only letters

Register With Nonmatching Password And Password Confirmation
    Set Username  testitesti
    Set Password  kalle123
    Set Password Confirmation  kalle111
    Submit Credentials
    Register Should Fail With Message  Invalid password confirmation

Login After Successful Registration
    Set Username  testitesti
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Succeed
    Go To Login Page
    Set Username  testitesti
    Set Password  kalle123
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  kalle
    Set Password  password
    Set Password Confirmation  password
    Submit Credentials
    Register Should Fail With Message  Password cannot contain only letters
    Go To Login Page
    Set Username  kalle
    Set Password  password
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password


*** Keywords ***

Submit Credentials
    Click Button  Register

Register Should Succeed
    Welcome Page Should Be Open

Go To Register Page
    Register Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Page Should Contain  ${message}