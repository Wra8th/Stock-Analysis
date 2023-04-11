function Form(){

    const [quoteno, setquoteno] = useState(0);
    var jsonData = {
        "users": [
            {
                "name": "alan", 
                "age": 23,
                "username": "aturing"
            },
            {
                "name": "john", 
                "age": 29,
                "username": "__john__"
            }
        ]
      }
    function handleClick(){
        fetch("/request_data",{
            method: 'POST',
            mode: 'cors',
            body: JSON.stringify(jsonData)
        }).then(console.log("successful"))
    }
    return(
        <div onClick={handleClick} style={{
            textAlign: 'center',
            width: '100px',
            border: '1px solid gray',
            borderRadius: '5px'
          }}>
            Send data to backend
          </div>
    )
}

export default Form