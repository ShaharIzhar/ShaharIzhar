/* *****************************************************************************
 *  Name:
 *  Date:
 *  Description:
 **************************************************************************** */

/* *****************************************************************************
 *  Name:              Ada Lovelace
 *  Coursera User ID:  123456
 *  Last modified:     October 16, 1842
 **************************************************************************** */

import java.util.Iterator;
import java.util.NoSuchElementException;

public class Deque<Item> implements Iterable<Item> {
    private Node first;
    private Node last;
    private int numberOfItems;

    private class Node {
        private Item item;
        private Node next;
        private Node prev;

        Node(Item item) {
            this.item = item;
            this.next = null;
            this.prev = null;
        }
    }

    // construct an empty deque
    public Deque() {
        this.first = null;
        this.last = null;
        numberOfItems = 0;
    }

    // is the deque empty?
    public boolean isEmpty() {
        return numberOfItems == 0;
    }

    // return the number of items on the deque
    public int size() {
        return numberOfItems;
    }

    // add the item to the front
    public void addFirst(Item item) {
        if (item == null) throw new NullPointerException();
        if (this.isEmpty()) {
            this.first = new Node(item);
            this.last = first;
        }
        else {
            Node oldfirst = first;
            first = new Node(item);
            first.item = item;
            first.next = oldfirst;
        }
        numberOfItems++;

    }

    // add the item to the back
    public void addLast(Item item) {
        if (this.isEmpty()) {
            this.last = new Node(item);
            this.first = last;
        }
        else {
            Node oldLast = last;
            last = new Node(item);
            last.item = item;
            last.prev = oldLast;
        }
        numberOfItems++;
    }

    // remove and return the item from the front
    public Item removeFirst() {
        if (isEmpty()) throw new java.util.NoSuchElementException();
        Item item = first.item;
        first = first.next;
        numberOfItems--;
        if (isEmpty()) last = first;
        else first.prev = null;
        return item;
    }

    public Item removeLast() {
        if (isEmpty()) throw new java.util.NoSuchElementException();
        Item item = last.item;
        last = last.prev;
        numberOfItems--;
        if (isEmpty()) first = last;
        else last.next = null;
        return item;
    }

    // return an iterator over items in order from front to back
    public Iterator<Item> iterator() {
        return new DequeIterator();
    }

    private class DequeIterator implements Iterator<Item> {
        private Node current;

        public DequeIterator() {
            this.current = first;
        }

        public boolean hasNext() {
            return current != null;
        }

        public void remove() {
            throw new UnsupportedOperationException();
        }

        public Item next() {
            if (!this.hasNext()) {
                throw new NoSuchElementException();
            }
            else {
                Node node = current;
                current = current.next;
                return node.item;
            }
        }
    }

    public static void main(String[] args) {

    }

}


