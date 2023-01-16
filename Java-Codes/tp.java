import java.awt.*;
import java.awt.event.*;

class MyFrame extends Frame implements WindowListener
{
  MyFrame()
   {
     addWindowListener(this);
   }
  public void windowOpened(WindowEvent we)
   {
     setBackground(Color.red);
   }
  public void windowClosing(WindowEvent we)
   {
     setVisible(false);
     dispose();
   }
  public void windowClosed(WindowEvent we)
   {
   }
  public void windowActivated(WindowEvent we)
   {
     setBackground(Color.cyan);
   }
  public void windowDeactivated(WindowEvent we)
   {
     setBackground(Color.black);
   }
  public void windowIconified(WindowEvent we)
   {
     setTitle("Minimized");
   }
  public void windowDeiconified(WindowEvent we)
   {
     setTitle("Maximized");
   }
}
class Demo
{
 public static void main(String args[ ]) 
  {
    MyFrame m=new MyFrame();
    m.setSize(300, 300);
    m.setVisible(true);    
  }
}
