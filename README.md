# Zé Delivery - QA Challenge

Você pode ler esta documentação, em portugês,
[clicando aqui.](docs/LEIAME.md)

**The first challenge is identity 3 important flows that keep the application working properly. I've identified these:**

- **Inform Address:** If the user can't enter address, he will not know if the Zé delivery service will be available in his region. And if it's available, the products will not be displayed in this case, because they are displayed to the user according to the coverage served in the region. 

-  **Payment:** If the payment services has unavailabe, the purchase can't be completed and the order can't be created. 

- **Cart:** If the products selected by the user are not being updated and calculated correctly in the cart, it will cause inconvenience for the user who can withdraw from the purchase. 




