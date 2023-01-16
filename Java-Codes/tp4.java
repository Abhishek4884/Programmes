 class Animal {
      void makeSound() {
        System.out.println("Some generic animal sound");
    }
    void makeSound1() {
        System.out.println("Some generic animal sound-----------------");
    }
}

 class Cat extends Animal {
     void makeSound() {
        System.out.println("Meow");
    }
}

public class tp4
{
    public static void main(String[] args) {
        Animal a = new Animal();
        Cat c = new Cat();
        c.makeSound();
        a.makeSound();
        c.makeSound1();
    }
}