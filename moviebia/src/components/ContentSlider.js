import classes from './ContentSlider.module.scss';
import MoviePoster from './MoviePoster';
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import Slider from 'react-slick';
const ContentSlider = (props) => {
    const settings = {
        dots: true,
        infinite: true,
        speed: 500,
        slidesToShow: 6

        ,
        slidesToScroll: 3
    };

    return (<>
        <div >
            <h2>Suggested For You</h2>
            <Slider {...settings} className={classes.slider}>
                <div className={classes.posterDiv}><MoviePoster /></div><div className={classes.posterDiv}><MoviePoster /></div><div className={classes.posterDiv}><MoviePoster /></div><div className={classes.posterDiv}><MoviePoster /></div><div className={classes.posterDiv}><MoviePoster /></div><div className={classes.posterDiv}><MoviePoster /></div><div className={classes.posterDiv}><MoviePoster /></div><div className={classes.posterDiv}><MoviePoster /></div></Slider>
        </div>
    </>);
}
export default ContentSlider;


