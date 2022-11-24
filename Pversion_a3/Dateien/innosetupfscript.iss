; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "DSALoot"
#define MyAppVersion "A.4"
#define MyAppPublisher "Kjell"
#define MyAppExeName "DSALoot.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{1AD960E3-91C1-490D-AE01-7FFFAE819602}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={autopf}\{#MyAppName}
DisableProgramGroupPage=yes
; Remove the following line to run in administrative install mode (install for all users.)
PrivilegesRequired=lowest
OutputDir=C:\Users\D�ner\Desktop
OutputBaseFilename=DSA_Loot Setup
SetupIconFile=E:\kjell\Dokumente\Hobby\Programmieren\Quelltexte\Python\Loot\Pversion_a3\Dateien\Fox.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "german"; MessagesFile: "compiler:Languages\German.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "E:\kjell\Dokumente\Hobby\Programmieren\Quelltexte\Python\Loot\Pversion_a4\Dateien\DSALoot V.a4\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "E:\kjell\Dokumente\Hobby\Programmieren\Quelltexte\Python\Loot\Pversion_a4\Dateien\DSALoot V.a4\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

