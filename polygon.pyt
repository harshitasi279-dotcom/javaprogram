abstract class Polygon {

    double side;

    Polygon(double side) {
        this.side = side;
    }

    abstract void area();
}


class Pentagon extends Polygon {

    Pentagon(double side) {
        super(side);
    }

    void area() {
        double result = (5 * side * side) / (4 * Math.tan(Math.PI / 5));

        System.out.println("Area of Pentagon = " + result);
    }
}


class Hexagon extends Polygon {

    Hexagon(double side) {
        super(side);
    }

    void area() {
        double result = (3 * Math.sqrt(3) * side * side) / 2;

        System.out.println("Area of Hexagon = " + result);
    }
}


public class PolygonDemo {

    public static void main(String[] args) {

        Polygon p1 = new Pentagon(5);
        Polygon p2 = new Hexagon(5);

        p1.area();
        p2.area();
    }
}