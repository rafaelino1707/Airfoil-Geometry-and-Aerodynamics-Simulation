import java.awt.image.BufferedImage;
import javax.imageio.ImageIO;
import javax.swing.*;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.awt.*;
import java.io.*;

public class MainJavaInterface {



    /* ---------------------------------------==========(+)==========---------------------------------------  */

    // main Function
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            System.out.println("Diretório atual: " + System.getProperty("user.dir"));

            // Creating the main Frame Used for the Interface
            JFrame frame0 = new JFrame("Airfoil Geometry and Aerodynamics Simulator");
            frame0.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame0.setExtendedState(JFrame.MAXIMIZED_BOTH);
            frame0.getContentPane().setBackground(Color.WHITE);

            // Creating the Initial Panel (Menu)
            JPanel mainPanel = createMainPanel(frame0);
            frame0.add(mainPanel);
            frame0.setVisible(true);
        });
    }

    private static JPanel createMainPanel(JFrame frame) {
    JPanel mainPanel = new JPanel();
    mainPanel.setLayout(null); // Permite usar coordenadas absolutas
    mainPanel.setBackground(Color.WHITE);

    // Título "NACA..."
    JLabel titleLabel = new JLabel("NACA Airfoil Input");
    titleLabel.setFont(new Font("SansSerif", Font.BOLD, 28));
    titleLabel.setForeground(new Color(10, 10, 10));
    titleLabel.setBounds(100, 50, 400, 40); // x, y, largura, altura
    mainPanel.add(titleLabel);

    // Label do campo de texto
    JLabel label1 = new JLabel("Enter NACA code:");
    label1.setFont(new Font("SansSerif", Font.PLAIN, 16));
    label1.setForeground(new Color(30, 30, 20));
    label1.setBounds(100, 110, 150, 30);
    mainPanel.add(label1);

    // Caixa de texto
    JTextField textField1 = new JTextField();
    textField1.setBounds(260, 110, 120, 30);
    mainPanel.add(textField1);

    return mainPanel;
}

}