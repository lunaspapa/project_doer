const GET_GOALS = 'get/getGoals';
const POST_GOAL = 'post/postGoal';
const UPDATE_GOAL = 'update/updateGoal';
const DELETE_GOAL = 'delete/deleteGoal';

const get = (payload) => ({
  type: GET_GOALS,
  payload
});

const post = (payload) => ({
  type: POST_GOAL,
  payload
});

const update = (payload) => ({
  type: UPDATE_GOAL,
  payload
});

const del = (payload) => ({
  type: DELETE_GOAL,
  payload
})

export const getGoals = (userID) => async dispatch => {
  const res = await fetch(`/api/goals/${userID}`);
  if (res.ok) {
    const data = await res.json();
    dispatch(get(data));
    return data;
  } else {
    return {
      "Message": "Unsuccessful"
    }
  }
};

export const postGoal = (payload) => async dispatch => {
  const res = await fetch(`/api/goals/new`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  });
  if (res.ok) {
    const data = await res.json();
    dispatch(post(data));
    return data;
  } else {
    return {
      "Message": "Unsuccessful"
    }
  }
};

export const updateGoal = (payload) => async dispatch => {
  const res = await fetch(`/api/goals/${payload.goalID}/update`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  });
  if (res.ok) {
    const data = await res.json();
    dispatch(update(data));
    return data;
  } else {
    return {
      "Message": "Unsuccessful"
    }
  }
};

export const uptickStreak = (goalID) => async dispatch => {
  const res = await fetch(`/api/goals/${goalID}/update/streak`)
  if (res.ok) {
    const data = await res.json();
    dispatch(getGoals(data));
    return data;
  } else {
    return {
      "Message": "Unsuccessful"
    }
  }
};

export const completeGoal = (goalID) => async dispatch => {
  const res = await fetch(`/api/goals/${goalID}/update/complte`)
  if (res.ok) {
    const data = await res.json();
    dispatch(getGoals(data));
    return data;
  } else {
    return {
      "Message": "Unsuccessful"
    }
  }
};


export const deleteGoal = (goalID) => async dispatch => {
  const res = await fetch(`/api/goals/${goalID}/delete`, {
    method: 'DELETE',
    headers: { 'Content-Type': 'application/json' },
  });
  if (res.ok) {
    const data = await res.json();
    dispatch(del(data));
    return data;
  } else {
    return {
      "Message": "Unsuccessful"
    }
  }
};

const goalReducer = (state = {}, action) => {
  let newState = { ...state };
  switch (action.type) {
    case GET_GOALS:
      newState = {}
      action.payload.goals.forEach(goal => newState[goal.id] = goal);
      return newState
    case POST_GOAL:
      newState[action.payload.id] = action.payload
      return newState
    case UPDATE_GOAL:
      newState[action.payload.id] = action.payload
      return newState
    case DELETE_GOAL:
      delete newState[action.payload.id]
      return newState
    default:
      return state
  }
};

export default goalReducer;
