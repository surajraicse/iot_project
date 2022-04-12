'use strict';
const e = React.createElement;

function App() {
  return (
    <div>
      <h1>Hello, World!</h1>
    </div>
  );
}

const domContainer = document.querySelector('#reactAppContainer');
ReactDOM.render(
  e(App),
  domContainer
);