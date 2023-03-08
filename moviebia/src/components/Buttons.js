import classes from "./Buttons.module.css";
const Buttons = (props) => {
    const st = { "--color": props.color };
    return (
        <>
            <div className={classes.container}>
                <a onClick={props.clickhandler} className={classes.button} style={st}><span></span>
                    <span></span>
                    <span></span>
                    <span></span>{props.children}</a></div></>)
}
export default Buttons;