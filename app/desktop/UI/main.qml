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
 
        // Поле ввода первого числа
        TextField {
            id: firstNumber
            Layout.fillWidth: true
        }
 
        Text {
            text: qsTr("Пароль")
            Layout.fillWidth: true
            color: "#FFFFFF"
            font.pointSize: 24
            horizontalAlignment: Text.AlignHCenter
        }
 
        // Поле ввода второго числа
        TextField {
            id: secondNumber
            Layout.fillWidth: true
            echoMode: TextInput.Password
        }
 
        Button {
            height: 40
            Layout.fillWidth: true
            text: qsTr("Войти")
 
 
            onClicked: {
                // Вызываем слот калькулятора, чтобы сложить числа
                calculator.sum(firstNumber.text, secondNumber.text)
            }
        }

        Text {
            id: sumResult
            color: "#FFFFFF"
            font.pointSize: 10
            horizontalAlignment: Text.AlignHCenter
        }
    }

    Connections {
        target: calculator
 
        // Обработчик сигнала сложения
        onSumResult: {
            // sum было задано через arguments=['sum']
            sumResult.text = sum
        }
 
    }

}