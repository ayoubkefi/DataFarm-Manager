import { BrowserRouter, Route, Routes } from "react-router-dom";
import { OperatorPage } from "./pages/OperatorPage";

function App() {
  return (
  <BrowserRouter>
    <Routes>
      <Route path="/operators" element = {<OperatorPage/>} />
    </Routes>
  </BrowserRouter>
  )
}

export default App