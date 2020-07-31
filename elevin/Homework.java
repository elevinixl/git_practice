package test;
import java.util.Arrays;

public class Homework {

    public static void main(String[] args) {
        System.out.println("Hello World!");

        // Question 1a
        int[] nums = {1,2,3,4};
        swap1(nums);
        System.out.println(Arrays.toString(nums));

        // Question 1b
        String[] words = {"Hi","Ed","Something"};
        swap2(words);
        System.out.println(Arrays.toString(words));

        // Question 2
        System.out.println(listSum(nums));

        // Question 3
        System.out.println(maxNum(nums));

        //Question 4
        int[] nums2 = {3, 2, 1, 5};
        System.out.println(sameElements(nums, nums2));
        System.out.println(sameElements(nums, nums));

        //Question 5
        System.out.println(firstInstance(nums2,5));

        //Question 6
        System.out.println("Larger numbers:");
        largerNumbers(nums2, 2);
    }

    private static void swap1(int[] list1) {
        int length = list1.length;
        int first = list1[0];
        list1[0] = list1[length - 1];
        list1[length - 1] = first;
    }

    private static void swap2(String[] list2) {
        int length = list2.length;
        String first = list2[0];
        list2[0] = list2[length - 1];
        list2[length - 1] = first;
    }

    private static int listSum(int[] listA) {
        int sum = 0;
        for (int i = 0; i < listA.length; i++) {
            sum += listA[i];
        }
        return sum;
    }

    private static int maxNum(int[] listA) {
        int currentMax = 0;
        for (int i = 0; i < listA.length; i++) {
            if (currentMax < listA[i]) {
                currentMax = listA[i];
            }
        }
        return currentMax;
    }

    private static boolean sameElements(int[] listA, int[] listB) {
        int lenA = listA.length;
        int lenB = listB.length;
        if (lenA != lenB) {
            return false;
        }
        for (int i = 0; i < lenA; i++) {
            if (listA[i] != listB[i]) {
                return false;
            }
        }
        return true;
    }

    private static int firstInstance(int[] listA, int element) {
        for (int i = 0; i < listA.length; i++) {
            if (element == listA[i]) {
                return i;
            }
        }
        return 0;
    }

    private static void largerNumbers(int[] listA, int referenceInt) {
        for (int i = 0; i < listA.length; i++) {
            if (listA[i] > referenceInt) {
                System.out.println(listA[i]);
            }
        }
    }
}
