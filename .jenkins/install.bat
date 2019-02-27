python -m venv conan || goto :error
conan\Scripts\pip install conan || goto :error
conan\Scripts\pip install conan_package_tools || goto :error

conan\Scripts\conan user || goto :error
goto :EOF

:error
echo Failed with error #%errorlevel%.
exit /b %errorlevel%
