package RunningButton;

import javax.swing.*;
import java.awt.*;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MyFrame {
    MyFrame(){
        JFrame frame = new JFrame();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(600, 600);
        frame.setLocation(400, 100);
        frame.setTitle("Поставите ли 5 автоматом за экзамен?)");
        //frame.setIconImage(new ImageIcon(getClass().getResource("Images/icon.png")).getImage());
        frame.setLayout(new GridBagLayout());


        JButton button = new JButton("ДА");
        JButton button2 = new JButton("НЕА, ФИГ ТЕБЕ");

        Font fnutton = new Font("Arial", Font.BOLD, 16);
        button.setFont(fnutton);
        button2.setFont(fnutton);

        button.setBackground(Color.GREEN);
        button2.setBackground(Color.RED);
        button.setCursor(new Cursor(Cursor.HAND_CURSOR));
        button2.setCursor(new Cursor(Cursor.HAND_CURSOR));

        button2.addMouseListener(new MouseAdapter() {
            @Override
            public void mouseEntered(MouseEvent e) {
                int x = (int) (Math.random() * 500); // генерируем случайное значение координаты x в пределах ширины окна
                int y = (int) (Math.random() * 500); // генерируем случайное значение координаты y в пределах высоты окна
                button2.setLocation(x, y); // изменяем положение кнопки на экране
            }
        });

        button.addActionListener(e -> {
            Font BigFontTR = new Font("TimesRoman", Font.BOLD, 80);
            JButton button3 = new JButton("ЗАШИБИСЬ!");
            button3.setFont(BigFontTR);
            button3.setBackground(Color.GREEN);
            frame.setLayout(new BorderLayout());
            frame.add(button3, BorderLayout.CENTER);
            frame.validate();
            frame.remove(button);
            frame.remove(button2);
            frame.revalidate();
            frame.repaint();
        });
        button2.addActionListener(e -> {
            Font BigFontTR = new Font("TimesRoman", Font.BOLD, 80);
            JButton button4 = new JButton("НЕЗАШИБИСЬ =(!");
            button4.setFont(BigFontTR);
            button4.setBackground(Color.RED);
            frame.setLayout(new BorderLayout());
            frame.add(button4, BorderLayout.CENTER);
            frame.validate();
            frame.remove(button);
            frame.remove(button2);
            frame.revalidate();
            frame.repaint();
        });
        frame.add(button);
        frame.add(button2);

        frame.setVisible(true);

    }
}

