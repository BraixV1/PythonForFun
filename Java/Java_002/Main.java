// Java learning 002 GUI
package Java.Java_002;
import javax.swing.JOptionPane;

public class Main {

    public static void main(String[] args) {
        
        String name = JOptionPane.showInputDialog("Enter your name");
        JOptionPane.showMessageDialog(null, "Hello"+name, name, 0, null);

        int age = Integer.parseInt(JOptionPane.showInputDialog("Enter your age"));
        JOptionPane.showMessageDialog(null, "You are "+age+" old");

        double height = Double.parseDouble(JOptionPane.showInputDialog("Enter your height"));
        JOptionPane.showMessageDialog(null, "You are "+height+" cm tall");
    }
}
