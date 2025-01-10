# Django Signals

**Signals: Using Signals for Event-Driven Architecture**

Django’s signals allow certain senders to notify a set of receivers when specific actions have taken place, facilitating decoupled applications by allowing components to communicate without tight integration.

**Key Concepts**:

* **Signal**: A message sent by a sender that indicates something has occurred.
* **Receiver**: A function connected to a signal that performs an action when the signal is sent.
* **Built-in Signals**: Django provides built-in signals like pre_save, post_save, pre_delete, and post_delete.

**Use Cases**:

* Automatically updating related models when a model is saved.
* Sending notifications when a new user registers.
* Cleaning up resources when an object is deleted.