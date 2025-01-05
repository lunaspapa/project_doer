import { configureStore, combineReducers, applyMiddleware, compose } from 'redux';
import { thunk } from 'redux-thunk';
import session from './session';
import goalReducer from './goal';

const rootReducer = combineReducers({
  session,
  goalReducer
});

let enhancer;

if (process.env.NODE_ENV === 'production') {
  enhancer = applyMiddleware(thunk);
} else {
  const logger = require('redux-logger').default;
  const composeEnhancers =
    window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
  enhancer = composeEnhancers(applyMiddleware(thunk, logger));
}

const createStore = (preloadedState) => {
  return configureStore(rootReducer, preloadedState, enhancer);
};

export default createStore;
