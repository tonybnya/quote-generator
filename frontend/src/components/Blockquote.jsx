import React from "react";

const Blockquote = ({ author, quote }) => {
  return (
    <figure className="max-w-screen-md mx-auto text-center py-12">
      <blockquote>
        <p className="text-2xl italic font-medium text-gray-900 dark:text-white">
          {quote}
        </p>
      </blockquote>
      <figcaption className="flex items-center justify-center mt-6 space-x-3 rtl:space-x-reverse">
        <div className="flex items-center divide-x-2 rtl:divide-x-reverse divide-gray-500 dark:divide-gray-700">
          <cite className="pe-3 font-medium text-gray-900 dark:text-white">
            — {author}.
          </cite>
        </div>
      </figcaption>
    </figure>
  );
};

export default Blockquote;
