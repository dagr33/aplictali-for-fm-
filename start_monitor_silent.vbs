' ════════════════════════════════════════════════════════════════════════════
' ՌԱԴԻՈ ՄՈՆԻՏՈՐԻՆԳ - Silent Background Launcher (VBScript)
' ════════════════════════════════════════════════════════════════════════════
'
' Այս ֆայլը գործարկում է մոնիտորինգը լիովին ցածր պրոֆիլում
' Բացlouis թողիր այս ֆայլը, և ծրագիրը կսկսվի ֆոնային ռեժիմում
'

Set objShell = CreateObject("WScript.Shell")
Set objFSO = CreateObject("Scripting.FileSystemObject")

' Ստանալ ընթացիկ ուղղությունը
currentDir = objFSO.GetParentFolderName(WScript.ScriptFullName)

' Ստուգել Python-ը
Set objExec = objShell.Exec("python --version")
If objExec.Status <> 0 Then
    MsgBox "❌ Python-ը չի գտնվել! Տեղադրիր Python։ https://www.python.org/downloads/", vbCritical, "Error"
    WScript.Quit 1
End If

' Ստուգել schedule պակետը
Set objExec = objShell.Exec("pip show schedule")
If objExec.Status <> 0 Then
    objShell.Run "pip install schedule", 0, True
End If

' Գործարկել Python ֆոնային ռեժիմում
pythonScript = currentDir & "\radio_monitor_complete.py"
objShell.Run "pythonw """ & pythonScript & """", 0, False

' Ցուցակցել հաղորդագրություն
MsgBox "✅ Ռադիո մոնիտորինգը սկսված է ֆոնային ռեժիմում" & vbCrLf & vbCrLf & "Ծրագիրը գործարկվում է ֆոնային պրոցեսում։" & vbCrLf & "Այն կուցադրի ծանուցումներ անհրաժեշտ լինելու դեպքում։", vbInformation, "Radio Monitor Started"

WScript.Quit 0
