package myFirstDesktopApp;
import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;
import javax.swing.*;
import javax.swing.border.*;
import javax.swing.tree.DefaultMutableTreeNode;
import java.awt.*;
import java.awt.event.*;
import java.io.File;
import java.io.InputStream;

public class MyApplication {
    private JTree tree;
    private int count = 0;
    MyApplication(){
//        try {
//            UIManager.setLookAndFeel("javax.swing.plaf.nimbus.NimbusLookAndFeel");
//        } catch(Exception ignored){}
        //Container container = new Container();
        JFrame frame = new JFrame();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(600, 650);
        frame.setLocation(500, 150);
        frame.setLayout(new BorderLayout());
        frame.setTitle("Application");
        //Работа с меню
        JMenuBar menuBar = new JMenuBar();
        JMenu menu = new JMenu("Файл");
        JMenu menu2 = new JMenu("Правка");
        JMenu menu3 = new JMenu("Метка");

        JMenuItem menuItem1 = new JMenuItem("Открыть");
        menu.add(menuItem1);

        JMenuItem menuItem2 = new JMenuItem("Создать");
        menu.add(menuItem2);

        JMenuItem menuItem7 = new JMenuItem("Сохранить как");
        menu.add(menuItem7);

        menu.addSeparator(); // line to separate different items types
        JRadioButtonMenuItem menuItem3 = new JRadioButtonMenuItem("Сохранить файл автоматически");
        menu.add(menuItem3);

        JRadioButtonMenuItem menuItem4 = new JRadioButtonMenuItem("Не сохранять файл автоматически");
        menu.add(menuItem4);

        JMenuItem menuItem5 = new JMenuItem("Копировать");
        menu2.add(menuItem5);

        JMenuItem menuItem6 = new JMenuItem("Удалить");
        menu2.add(menuItem6);

        JMenuItem menuItem8 = new JMenuItem("Вставить");
        menu2.add(menuItem8);

        menu3.addSeparator(); // line to separate different items types
        JRadioButtonMenuItem menu3Item1 = new JRadioButtonMenuItem("Поставить метку");
        menu3.add(menu3Item1);

        JRadioButtonMenuItem menu3Item2 = new JRadioButtonMenuItem("Удалить метку");
        menu3.add(menu3Item2);

        menuBar.add(menu);
        menuBar.add(menu2);
        menuBar.add(menu3);
        frame.setJMenuBar(menuBar);
        //Работа с деревом
        DefaultMutableTreeNode root = new DefaultMutableTreeNode("Root");
        DefaultMutableTreeNode users = new DefaultMutableTreeNode("Users");

        DefaultMutableTreeNode package1 = new DefaultMutableTreeNode("Folder1");
        package1.add(new DefaultMutableTreeNode("File1"));
        package1.add(new DefaultMutableTreeNode("File2"));
        package1.add(new DefaultMutableTreeNode("File3"));
        package1.add(new DefaultMutableTreeNode("File4"));

        DefaultMutableTreeNode package2 = new DefaultMutableTreeNode("Folder2");
        package2.add(new DefaultMutableTreeNode("File5"));
        package2.add(new DefaultMutableTreeNode("File6"));
        package2.add(new DefaultMutableTreeNode("File7"));
        package2.add(new DefaultMutableTreeNode("File8"));
        package2.add(new DefaultMutableTreeNode("File9"));

        DefaultMutableTreeNode package3 = new DefaultMutableTreeNode("Folder3");
        package3.add(new DefaultMutableTreeNode("File10"));
        package3.add(new DefaultMutableTreeNode("File11"));

        DefaultMutableTreeNode package4 = new DefaultMutableTreeNode("Folder4");
        package3.add(package4);
        package4.add(new DefaultMutableTreeNode("File12"));
        DefaultMutableTreeNode package5 = new DefaultMutableTreeNode("Folder5");
        package5.add(new DefaultMutableTreeNode("File10"));
        package5.add(new DefaultMutableTreeNode("File11"));
        package4.add(package5);
        root.add(package1);
        root.add(package2);
        root.add(package3);

        tree = new JTree(root);
        frame.add(tree);
        //Создание инструментов
        JToolBar toolBar = new JToolBar();
        JButton button1 = new JButton("Nimbus");
        button1.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try {
                    UIManager.setLookAndFeel("javax.swing.plaf.nimbus.NimbusLookAndFeel");
                    SwingUtilities.updateComponentTreeUI(frame);
                } catch(Exception el){
                    el.printStackTrace();
                }
            }
        });
        JButton button2 = new JButton("Metal");
        button2.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try {
                    UIManager.setLookAndFeel("javax.swing.plaf.metal.MetalLookAndFeel");
                    SwingUtilities.updateComponentTreeUI(frame);
                } catch(Exception el){
                    el.printStackTrace();
                }
            }
        });
        JButton button3 = new JButton("CDE/Motif");
        button3.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try {
                    UIManager.setLookAndFeel("com.sun.java.swing.plaf.motif.MotifLookAndFeel");
                    SwingUtilities.updateComponentTreeUI(frame);
                } catch(Exception el){
                    el.printStackTrace();
                }
            }
        });
        JButton button4 = new JButton("Windows");
        button4.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try {
                    UIManager.setLookAndFeel("com.sun.java.swing.plaf.windows.WindowsLookAndFeel");
                    SwingUtilities.updateComponentTreeUI(frame);
                } catch(Exception el){
                    el.printStackTrace();
                }
            }
        });
        JButton button5 = new JButton("Windows Classic");
        button5.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try {
                    UIManager.setLookAndFeel("com.sun.java.swing.plaf.windows.WindowsClassicLookAndFeel");
                    SwingUtilities.updateComponentTreeUI(frame);
                } catch(Exception el){
                    el.printStackTrace();
                }
            }
        });
        JButton button6 = new JButton("EXIT");
        button6.addActionListener(e -> {
            System.exit(0);
        });
        JButton button7 = new JButton("ChipiChapa?)");
        button7.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                try {
                    // Загрузка GIF-изображения из ресурсов
                    InputStream gifStream = getClass().getResourceAsStream("Chipi_Chapa.gif");
                    ImageIcon icon = new ImageIcon(gifStream.readAllBytes());

                    // Создание нового окна, отображающего GIF
                    JFrame gifFrame = new JFrame("GIF");
                    JLabel label = new JLabel(icon);
                    gifFrame.add(label);
                    gifFrame.pack();
                    gifFrame.setVisible(true);

                    File file = new File("Chipi_Chapa.gif.mp4"); // Укажите путь к вашему звуковому файлу

                    Clip clip = AudioSystem.getClip();
                    AudioInputStream ais = AudioSystem.getAudioInputStream(file);
                    clip.open(ais);

                    clip.loop(Clip.LOOP_CONTINUOUSLY);

                    // Создаем таймер, который закроет окно через 10 секунд
                    Timer timer = new Timer(12000, new ActionListener() {
                        public void actionPerformed(ActionEvent e) {
                            gifFrame.dispose(); // Закрыть окно
                            clip.stop(); // Остановить воспроизведение звука
                            clip.close(); // Освободить ресурсы Clip
                        }
                    });
                    timer.setRepeats(false); // Установить повторение таймера на один раз
                    timer.start(); // Запустить таймер

                } catch (Exception ex) {
                    ex.printStackTrace();
                }
            }
        });

        JButton button8 = new JButton("НЕНАЖИМАТЬ!");
        button8.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                String username = JOptionPane.showInputDialog("Введите имя пользователя:");
                String password = JOptionPane.showInputDialog("Введите пароль:");
                if (username != null && password != null && username.equals("secret") && password.equals("secret22")) {
                    try {
                        // Загрузка GIF-изображения из ресурсов
                        InputStream gifStream = getClass().getResourceAsStream("");
                        ImageIcon icon = new ImageIcon(gifStream.readAllBytes());

                        // Создание нового окна, отображающего GIF
                        JFrame gifFrame = new JFrame("GIF");
                        JLabel label = new JLabel(icon);
                        gifFrame.add(label);
                        gifFrame.pack();
                        gifFrame.setVisible(true);

                        File file = new File(""); // Укажите путь к вашему звуковому файлу

                        Clip clip = AudioSystem.getClip();
                        AudioInputStream ais = AudioSystem.getAudioInputStream(file);
                        clip.open(ais);

                        clip.loop(Clip.LOOP_CONTINUOUSLY);

                        // Добавляем слушателя событий к фрейму
                        gifFrame.addWindowListener(new WindowAdapter() {
                            public void windowClosing(WindowEvent e) {
                                clip.stop(); // Остановить воспроизведение звука
                                clip.close(); // Освободить ресурсы Clip
                            }
                        });

                    } catch (Exception ex) {
                        ex.printStackTrace();
                    }
                } else {
                    // Неправильные учетные данные, ничего не происходит
                    JOptionPane.showMessageDialog(null, "Неправильное имя пользователя или пароль", "Ошибка", JOptionPane.ERROR_MESSAGE);
                }
            }
        });


        button1.setBackground(Color.WHITE);
        button2.setBackground(Color.GREEN);
        button3.setBackground(Color.magenta);
        button4.setBackground(Color.WHITE);
        button5.setBackground(Color.WHITE);
        button6.setBackground(Color.RED);
        button7.setBackground(Color.WHITE);
        button8.setBackground(Color.RED);

        toolBar.add(button1);
        toolBar.add(button2);
        toolBar.add(button3);
        toolBar.add(button4);
        toolBar.add(button5);
        toolBar.add(button6);
        toolBar.add(button7);
        toolBar.add(button8);


        frame.add(toolBar, BorderLayout.NORTH);
        frame.add(this.splitPane());

        frame.setVisible(true);
    }
    private JSplitPane splitPane() {
        JSplitPane splitPane = new JSplitPane();
        splitPane.setLeftComponent(new JScrollPane(buildPanelTree(this.tree)));
        splitPane.setRightComponent(new JScrollPane(buildScrollPanel()));
        return splitPane;
    }
    private JPanel buildPanelTree(JTree tree){
        JPanel panel = new JPanel(new BorderLayout());
        panel.setBorder(getBorder("FileTree"));
        panel.setBackground(Color.WHITE);
        panel.add(tree, BorderLayout.WEST);
        return panel;
    }
    private JScrollPane buildScrollPanel() {
        JTabbedPane jTabbedPane = new JTabbedPane(SwingConstants.TOP);
        jTabbedPane.setBackground(Color.white);

        JPanel panel = new JPanel(new BorderLayout());

        JPanel topPanel = new JPanel();
        JButton button = new JButton("0");
        JButton buttonzero = new JButton("Reset the clicker");
        JButton clearbuttton = new JButton("Сlear the playing field");



        buttonzero.addActionListener(e -> {
            count = 0;
            button.setText(Integer.toString(count));
        });

        button.addActionListener(e -> {
            count++;
            button.setText(Integer.toString(count));
        });
        topPanel.add(clearbuttton, 0);
        topPanel.add(button);
        topPanel.add(buttonzero);


        panel.add(topPanel, BorderLayout.NORTH);

        Panel specialpanel = new Panel();
        specialpanel.setLayout(new GridLayout(3, 3, 3, 3));

        JButton button1 = new JButton();
        button1.addMouseListener(new MouseAdapter() {
            @Override
            public void mousePressed(MouseEvent e) {
                if (SwingUtilities.isRightMouseButton(e)) {
                    button1.setText("O");
                } else if (SwingUtilities.isLeftMouseButton(e)) {
                    button1.setText("X");
                }
            }
        });
        JButton button2 = new JButton();
        button2.addMouseListener(new MouseAdapter() {
            @Override
            public void mousePressed(MouseEvent e) {
                if (SwingUtilities.isRightMouseButton(e)) {
                    button2.setText("O");
                } else if (SwingUtilities.isLeftMouseButton(e)) {
                    button2.setText("X");
                }
            }
        });
        JButton button3 = new JButton();
        button3.addMouseListener(new MouseAdapter() {
            @Override
            public void mousePressed(MouseEvent e) {
                if (SwingUtilities.isRightMouseButton(e)) {
                    button3.setText("O");
                } else if (SwingUtilities.isLeftMouseButton(e)) {
                    button3.setText("X");
                }
            }
        });
        JButton button4 = new JButton();
        button4.addMouseListener(new MouseAdapter() {
            @Override
            public void mousePressed(MouseEvent e) {
                if (SwingUtilities.isRightMouseButton(e)) {
                    button4.setText("O");
                } else if (SwingUtilities.isLeftMouseButton(e)) {
                    button4.setText("X");
                }
            }
        });
        JButton button5 = new JButton();
        button5.addMouseListener(new MouseAdapter() {
            @Override
            public void mousePressed(MouseEvent e) {
                if (SwingUtilities.isRightMouseButton(e)) {
                    button5.setText("O");
                } else if (SwingUtilities.isLeftMouseButton(e)) {
                    button5.setText("X");
                }
            }
        });
        JButton button6 = new JButton();
        button6.addMouseListener(new MouseAdapter() {
            @Override
            public void mousePressed(MouseEvent e) {
                if (SwingUtilities.isRightMouseButton(e)) {
                    button6.setText("O");
                } else if (SwingUtilities.isLeftMouseButton(e)) {
                    button6.setText("X");
                }
            }
        });
        JButton button7 = new JButton();
        button7.addMouseListener(new MouseAdapter() {
            @Override
            public void mousePressed(MouseEvent e) {
                if (SwingUtilities.isRightMouseButton(e)) {
                    button7.setText("O");
                } else if (SwingUtilities.isLeftMouseButton(e)) {
                    button7.setText("X");
                }
            }
        });
        JButton button8 = new JButton();
        button8.addMouseListener(new MouseAdapter() {
            @Override
            public void mousePressed(MouseEvent e) {
                if (SwingUtilities.isRightMouseButton(e)) {
                    button8.setText("O");
                } else if (SwingUtilities.isLeftMouseButton(e)) {
                    button8.setText("X");
                }
            }
        });
        JButton button9 = new JButton();
        button9.addMouseListener(new MouseAdapter() {
            @Override
            public void mousePressed(MouseEvent e) {
                if (SwingUtilities.isRightMouseButton(e)) {
                    button9.setText("O");
                } else if (SwingUtilities.isLeftMouseButton(e)) {
                    button9.setText("X");
                }
            }
        });
        clearbuttton.addActionListener(e -> {
            button1.setText("");
            button2.setText("");
            button3.setText("");
            button4.setText("");
            button5.setText("");
            button6.setText("");
            button7.setText("");
            button8.setText("");
            button9.setText("");
        });

        specialpanel.add(button1);
        specialpanel.add(button2);
        specialpanel.add(button3);
        specialpanel.add(button4);
        specialpanel.add(button5);
        specialpanel.add(button6);
        specialpanel.add(button7);
        specialpanel.add(button8);
        specialpanel.add(button9);
        //
        JPanel lastpanel = new JPanel(new GridLayout(0, 3, 10, 10)); // используем GridLayout для размещения кнопок

        // Создаем различные типы кнопок и добавляем их на панель
        JButton regularButton = new JButton("Обычная кнопка");
        lastpanel.add(regularButton);

        JToggleButton toggleButton = new JToggleButton("Переключаемая кнопка");
        lastpanel.add(toggleButton);

        JRadioButton radioButton = new JRadioButton("Радио кнопка");
        lastpanel.add(radioButton);

        JCheckBox checkBox = new JCheckBox("Флажок");
        lastpanel.add(checkBox);

        JButton htmlButton = new JButton("<html><b>HTML</b> кнопка</html>"); // Используем HTML для форматирования текста на кнопке
        lastpanel.add(htmlButton);
        //
        panel.add(specialpanel, BorderLayout.WEST);

        jTabbedPane.addTab("Activity", panel);
        jTabbedPane.addTab("Buttons", lastpanel);

        JTextArea text = new JTextArea();
        jTabbedPane.addTab("Text", text);

        String[] columnNames = {"Фамилия", "Имя", "Отчество"};
        Object[][] data = {
                {"Климкин", "Игорь", "Александрович"},
                {"Кондратенко", "Дмитрий", "Ярославович"},
                {"Иваков", "Андрей", "Валерьевич"}
        };

        JTable jTable = new JTable(data, columnNames);
        jTabbedPane.addTab("Table", jTable);

        jTabbedPane.setPreferredSize(new Dimension(100, 500));

        JPanel containerPanel = new JPanel(new BorderLayout());
        containerPanel.add(jTabbedPane, BorderLayout.NORTH);

        JScrollPane scrollpanel = new JScrollPane(containerPanel);
        scrollpanel.setVerticalScrollBarPolicy(JScrollPane.VERTICAL_SCROLLBAR_ALWAYS);
        scrollpanel.setHorizontalScrollBarPolicy(JScrollPane.HORIZONTAL_SCROLLBAR_ALWAYS);
        scrollpanel.setBorder(getBorder("MainWindow"));


        return scrollpanel;
    }
    private Border getBorder(String title) {
        Border etched = BorderFactory.createEtchedBorder(EtchedBorder.LOWERED);
        Border titledBorder = BorderFactory.createTitledBorder(etched, title);
        return titledBorder;
    }
}
