package Calculator;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

public class MyCalculator {
    double num1, num2;
    boolean flag = false;
    char operation;
    MyCalculator() {

        JFrame frame = new JFrame();
        frame.setLayout(new BorderLayout());
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(500, 650);
        frame.setLocation(450, 150);
        frame.setTitle("Calculator");

        frame.setIconImage(new ImageIcon(Main.class.getResource("calc.jpg").getPath()).getImage());
        try {
            UIManager.setLookAndFeel("com.sun.java.swing.plaf.windows.WindowsLookAndFeel");
            SwingUtilities.updateComponentTreeUI(frame);
        } catch(Exception el){
            el.printStackTrace();
        }

        // Панель для меню
        JMenuBar menuBar = new JMenuBar();
        JMenu menu = new JMenu("Меню");
        JMenuItem menuItem = new JMenuItem("Пункт меню");
        menu.add(menuItem);
        menuBar.add(menu);
        frame.setJMenuBar(menuBar);

        // Панель для ввода
        JPanel inputPanel = new JPanel();
        JTextField textField = new JTextField(45);
        textField.setFont(new Font("Arial", Font.PLAIN, 20));
        textField.setHorizontalAlignment(SwingConstants.CENTER);
        textField.setPreferredSize(new Dimension(30, 60)); // Устанавливаем предпочтительный размер
        textField.addKeyListener(new KeyListener() {
            @Override
            public void keyTyped(KeyEvent e) {
                char c = e.getKeyChar();
                if (!Character.isDigit(c) && c != '-') {
                    e.consume(); // отменить ввод символа, если он не является цифрой или одним из разрешенных символов
                }
            }

            @Override
            public void keyPressed(KeyEvent e) {
                // Не требуется реализация
            }

            @Override
            public void keyReleased(KeyEvent e) {
                // Не требуется реализация
            }
        });
        inputPanel.add(textField);

        // Панель для кнопок
        JPanel numpanel = new JPanel();
        GridLayout layout = new GridLayout(6, 4, 1, 1);
        numpanel.setLayout(layout);
        JButton[] buttons = {
                new JButton("n!"), new JButton("CE"), new JButton("C"), new JButton("<<"),
                new JButton("1/x"), new JButton("x^2"), new JButton("sqrt"), new JButton("/"),
                new JButton("7"), new JButton("8"), new JButton("9"), new JButton("*"),
                new JButton("4"), new JButton("5"), new JButton("6"), new JButton("-"),
                new JButton("1"), new JButton("2"), new JButton("3"), new JButton("+"),
                new JButton("+/-"), new JButton("0"), new JButton(","), new JButton("=")
        };
        buttons[0].addActionListener(e -> {
            double result = Double.parseDouble(textField.getText());
            if(result > 1) {
                for (int i = 2; i < Integer.parseInt(textField.getText()); i++) {
                    result *= i;
                }
                if (flag) {
                    num2 = result;
                    textField.setText(String.valueOf(num2));
                } else {
                    num1 = result;
                    textField.setText(String.valueOf(num1));
                }
            }
            else textField.setText("Факториал введен неверно!");

        });
        buttons[1].addActionListener(e -> {
            textField.setText("");
            this.num1 = 0;
            this.num2 = 0;
        });
        buttons[2].addActionListener(e -> {
            textField.setText("");
        });
        buttons[3].addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String text = textField.getText();
                if (text.length() > 0) {
                    textField.setText(text.substring(0, text.length() - 1));
                }
            }
        });
        buttons[4].addActionListener(e -> {
            if (flag){
                num2 = 1 / Double.parseDouble(textField.getText());
                textField.setText(String.valueOf(num2));
            }
            else {
                num1 = 1 / Double.parseDouble(textField.getText());
                textField.setText(String.valueOf(num1));

            }

        });
        buttons[5].addActionListener(e -> {
            if (flag){
                num2 = Math.pow(Double.parseDouble(textField.getText()), 2);
                textField.setText(String.valueOf(num2));
            }
            else {
                num1 = Math.pow(Double.parseDouble(textField.getText()), 2);
                textField.setText(String.valueOf(num1));
            }

        });
        buttons[6].addActionListener(e -> {
            if (flag){
                num2 = Math.sqrt(Double.parseDouble(textField.getText()));
                if(num2 > 0)
                    textField.setText(String.valueOf(num2));
                else textField.setText("Неверный ввод!");
            }
            else {
                num1 = Math.sqrt(Double.parseDouble(textField.getText()));
                if(num1 > 0)
                    textField.setText(String.valueOf(num1));
                else textField.setText("Неверный ввод!");
            }

        });
        buttons[7].addActionListener(e -> {
            num1 = Double.parseDouble(textField.getText());
            flag = true;
            textField.setText("");
            operation = '/';

        });
        buttons[8].addActionListener(e -> {
            textField.setText(textField.getText() + "7");
        });
        buttons[9].addActionListener(e -> {
            textField.setText(textField.getText() + "8");
        });
        buttons[10].addActionListener(e -> {
            textField.setText(textField.getText() + "9");
        });
        buttons[11].addActionListener(e -> {
            num1 = Double.parseDouble(textField.getText());
            flag = true;
            textField.setText("");
            operation = '*';
        });
        buttons[12].addActionListener(e -> {
            textField.setText(textField.getText() + "4");
        });
        buttons[13].addActionListener(e -> {
            textField.setText(textField.getText() + "5");
        });
        buttons[14].addActionListener(e -> {
            textField.setText(textField.getText() + "6");
        });
        buttons[15].addActionListener(e -> {
            num1 = Double.parseDouble(textField.getText());
            flag = true;
            textField.setText("");
            operation = '-';
        });
        buttons[16].addActionListener(e -> {
            textField.setText(textField.getText() + "1");
        });
        buttons[17].addActionListener(e -> {
            textField.setText(textField.getText() + "2");
        });
        buttons[18].addActionListener(e -> {
            textField.setText(textField.getText() + "3");
        });
        buttons[19].addActionListener(e -> {
            num1 = Double.parseDouble(textField.getText());
            flag = true;
            textField.setText("");
            operation = '+';
        });
        buttons[20].addActionListener(e -> {
            if(flag){
                num2 =  Double.parseDouble(textField.getText()) * -1;
                textField.setText(String.valueOf(num2));
            }
            else {
                num1 =  Double.parseDouble(textField.getText()) * -1;
                textField.setText(String.valueOf(num1));
            }
        });
        buttons[21].addActionListener(e -> {
            String text = textField.getText();
            if(textField.getText().length() == 0 || text.charAt(0) != 0)
                textField.setText(textField.getText() + "0");

        });
        buttons[22].addActionListener(e -> {
            if(textField.getText().length() == 1)
                textField.setText(textField.getText() + ".");

        });
        buttons[23].addActionListener(e -> {
            num2 = Double.parseDouble(textField.getText());
            if(operation == '+') {
                textField.setText(String.valueOf(num1 + num2));
            }
            else if(operation == '-') {
                textField.setText(String.valueOf(num1 - num2));
            }
            else if(operation == '*') {
                textField.setText(String.valueOf(num1 * num2));
            }
            else if(operation == '/') {
                if(num2 == 0){
                    textField.setText("На нуль делить нельзя!");
                }
                else textField.setText(String.valueOf(num1 / num2));
            }
            num2 = 0;
            num1 = 0;

        });
        for (JButton button : buttons) {
            button.setFont( new Font("Arial", Font.PLAIN, 16));
        }
        for (JButton button : buttons) {
            numpanel.add(button);
        }

        frame.add(inputPanel, BorderLayout.NORTH);
        frame.add(numpanel, BorderLayout.CENTER);

        frame.setVisible(true);
    }
}
