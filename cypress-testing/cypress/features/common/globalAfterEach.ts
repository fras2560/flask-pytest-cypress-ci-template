/**
 * Holds a global steps and hooks.
 * @packageDocumentation
 */

/** A hook that runs once before all tests. */
const globalAfter = (): void => {
    cy.log('Ran after each test');
};
afterEach(globalAfter);
