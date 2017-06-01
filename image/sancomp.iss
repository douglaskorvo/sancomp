; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "Sancomp"
#define MyAppVersion "1.1.b"
#define MyAppPublisher "Douglas Rodrigues"
#define MyAppExeName "sancomp.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{84DF0F45-49E9-49B9-B9D9-CD353ACD04F1}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={pf}\{#MyAppName}
DisableProgramGroupPage=yes
OutputDir=C:\complami\sancomp
OutputBaseFilename=Sancompx86v1.1.b
SetupIconFile=C:\complami\sancomp\build\exe.win32-2.7\image\sancomp.ico
WizardImageFile=C:\complami\sancomp\image\sancomp_logo1.bmp
Compression=lzma
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "brazilianportuguese"; MessagesFile: "compiler:Languages\BrazilianPortuguese.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked
Name: "quicklaunchicon"; Description: "{cm:CreateQuickLaunchIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked; OnlyBelowVersion: 0,6.1

[Files]
Source: "C:\complami\sancomp\build\exe.win32-2.7\sancomp.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\complami\sancomp\build\exe.win32-2.7\*"; DestDir: "{app}"; Flags: recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{commonprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{commondesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon
Name: "{userappdata}\Microsoft\Internet Explorer\Quick Launch\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: quicklaunchicon
Name: "{group}\Application"; Filename: "{app}\WinPython-32bit-2.7.13.0Zero\python-2.7.13\pythonw.exe"; WorkingDir: "{app}"; Parameters: """{app}\sancomp.py"""; IconFilename: "{app}\image\sancomp.ico"

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent
Filename: "{app}\WinPython-32bit-2.7.13.0Zero\python-2.7.13\python.exe"; WorkingDir: "{app}"; Parameters: """{app}\sancomp.py"""; Flags: runhidden

