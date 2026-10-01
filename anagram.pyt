import java.util.Scanner;

public class Anagram {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter first string: ");
        String str1 = sc.nextLine();

        System.out.print("Enter second string: ");
        String str2 = sc.nextLine();

        if (str1.length() != str2.length()) {
            System.out.println("The strings are not anagrams.");
        }
        else {

            char[] a = str1.toCharArray();
            char[] b = str2.toCharArray();

            // Sorting first character array
            for (int i = 0; i < a.length - 1; i++) {
                for (int j = i + 1; j < a.length; j++) {

                    if (a[i] > a[j]) {
                        char temp = a[i];
                        a[i] = a[j];
                        a[j] = temp;
                    }
                }
            }

            // Sorting second character array
            for (int i = 0; i < b.length - 1; i++) {
                for (int j = i + 1; j < b.length; j++) {

                    if (b[i] > b[j]) {
                        char temp = b[i];
                        b[i] = b[j];
                        b[j] = temp;
                    }
                }
            }

            boolean anagram = true;

            for (int i = 0; i < a.length; i++) {
                if (a[i] != b[i]) {
                    anagram = false;
                    break;
                }
            }

            if (anagram)
                System.out.println("The strings are anagrams.");
            else
                System.out.println("The strings are not anagrams.");
        }

        sc.close();
    }
}