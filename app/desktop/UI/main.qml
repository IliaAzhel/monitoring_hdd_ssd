import QtQuick 2.14
import QtQuick.Controls 2.14
import QtQuick.Layouts 1.2

ApplicationWindow {
    visible: true
    width: 400
    height: 600
    title: "Monitoring"

    
    
Rectangle {
        anchors.fill: parent
        
Image {
            sourceSize.width: parent.width
            sourceSize.height: parent.height
            source: "./hdd.jpg"
            fillMode: Image.PreserveAspectCrop
        }
        
Rectangle {
            anchors.fill: parent
            color: "transparent"
            
        }
    }

GridLayout {
        anchors.top: parent.top
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.topMargin: 50
        anchors.bottomMargin: 70
        anchors.margins: 15
 		anchors.horizontalCenter: parent.horizontalCenter
 		anchors.verticalCenter: parent.verticalCenter

        columns: 1
        rows: 1
        rowSpacing: 5
        columnSpacing: 1
 
        Text {
            text: qsTr("Логин")
            Layout.fillWidth: true
            color: "#FFFFFF"
            horizontalAlignment: Text.AlignHCenter
            font.pointSize: 24
        }
 

        TextField {
            id: login
            Layout.fillWidth: true
        }
 
        Text {
            text: qsTr("Пароль")
            Layout.fillWidth: true
            color: "#FFFFFF"
            font.pointSize: 24
            horizontalAlignment: Text.AlignHCenter
        }
 

        TextField {
            id: password
            Layout.fillWidth: true
            echoMode: TextInput.Password
        }
 
        Button {
            height: 40
            Layout.fillWidth: true
            text: qsTr("Войти")
 
 
            onClicked: {

                authentification.login(login.text, password.text)
            }
        }

        Text {
            id: authResult
            color: "#FFFFFF"
            font.pointSize: 10
            horizontalAlignment: Text.AlignHCenter
        }
    }

    Connections {
        target: authentification
 

        onAuthResult: {
            authResult.text = auth
        }
 
    }

}