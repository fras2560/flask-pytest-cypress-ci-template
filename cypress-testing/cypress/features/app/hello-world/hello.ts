import { When, Given } from 'cypress-cucumber-preprocessor/steps';

/** Acess the root url. */
const navigateToRoot = (): void => {
    cy.visit('');
};
Given(`I am on the root page`, navigateToRoot);

/** Assert hello world is visible. */
const assertHelloWorld = (): void => {
    cy.findByRole('heading', { name: /hello world/i }).should('be.visible');
};
When(`I see hello world`, assertHelloWorld);
